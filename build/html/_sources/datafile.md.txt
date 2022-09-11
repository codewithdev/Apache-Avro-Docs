
# DataFile Reader and Writer Python APIs

## Overview

The DataFileReader is an iterator that returns dicts corresponding to the serialized items. The Avro data is stored in a file along with its schema, so that files can be processed easily. The Avro data is written using the [DatumWriter](http://localhost:8000/io.html#datumreader-and-datumwriter-class) class. The Avro DataFileReader and DataFileWriter provides classes and methods to read and write Avro data files. Since each datum belongs to the same schema([See Schema Validation](http://localhost:8000/io.html#validating-avro-schema)), the data is categorized into groups called "blocks". A synchronization marker is generated between these blocks to read or write Avro data files. 

```{seealso}
 - [Avro Validation Python APIs](http://localhost:8000/io.html#validating-avro-schema)
 - [Avro Input/Output utilities and functions for DatumWriter and DatumReader Classes](http://localhost:8000/io.html#datumreader-and-datumwriter-class)
```

## Class DataFileWriter

DataFileWriter class implements writer interface for Avro data files. Since the data is grouped into blocks, so a synchronization is introduces between the blocks to split the files. This class contains the writer object that collect metadata and writes a datum to the buffer(if the schema exists).

<h3><i>DataFileWriter(object)</i></h3>

This class writes the Avro data files. If the schema exist, then we write to the file using the `DatumFileWriter`.

<h4>Code Example</h4>

```python
class DataFileWriter(object):
  @staticmethod
  def GenerateSyncMarker():
    return os.urandom(SYNC_SIZE)
```

<h3><i>__init__(self, writer, datum_writer, writer_schema=None,codec='null')</i></h3>

Construct a new DataFileReader instance and create metadata property. If the schema is not presents, we pass arguments to append property to the data file. The `__init__()` takes three arguments making the encoder to write to the file.

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `writer`
  - `string`
  - Object to write into.
* - `datum_writer`
  - `map`
  - Datum to write into. If the schema is present, the datum is appended to the file. Otherwise it is added to a new Avro data file.
 
* - `writer_schema`
  - object
  - By default None. Pass the schema object to write to the datum which is appended to the existing schema.
```

<h4>Code Example</h4>

```python
def __init__(
      self,
      writer,
      datum_writer,
      writer_schema=None,
      codec='null',
  ):
    
    self._writer = writer
    self._encoder = avro_io.BinaryEncoder(writer)
    self._datum_writer = datum_writer
    self._buffer_writer = io.BytesIO()
    self._buffer_encoder = avro_io.BinaryEncoder(self._buffer_writer)
    self._block_count = 0
    self._meta = {}

    # Ensure we have a writer that accepts bytes:
    self._writer.write(b'')

    # Whether the header has already been written:
    self._header_written = False

    if writer_schema is not None:
      if codec not in VALID_CODECS:
        raise DataFileException('Unknown codec: %r' % codec)
      self._sync_marker = DataFileWriter.GenerateSyncMarker()
      self.SetMeta('avro.codec', codec)
      self.SetMeta('avro.schema', str(writer_schema).encode('utf-8'))
      self.datum_writer.writer_schema = writer_schema
    else:
      # open writer for reading to collect metadata
      dfr = DataFileReader(writer, avro_io.DatumReader())

      # TODO: collect arbitrary metadata
      # collect metadata
      self._sync_marker = dfr.sync_marker
      self.SetMeta('avro.codec', dfr.GetMeta('avro.codec'))

      # get schema used to write existing file
      schema_from_file = dfr.GetMeta('avro.schema').decode('utf-8')
      self.SetMeta('avro.schema', schema_from_file)
      self.datum_writer.writer_schema = schema.Parse(schema_from_file)

      # seek to the end of the file and prepare for writing
      writer.seek(0, 2)
      self._header_written = True
```
## Read-only Properties

<h3><i>@property</i> writer(self)</h3>

Returns the writer that has been used by encoder to write to the file.

<h3><i>@property</i> encoder(self)</h3>

Returns the encoder that writes to the file and append the metadata to the datum associated with the schema.

<h3><i>@property</i> datum_writer(self)</h3>

Returns the datum writer that writes to the file.

<h4>Code Example</h4>

```python
@property
  def writer(self):
    return self._writer

  @property
  def encoder(self):
    return self._encoder

  @property
  def datum_writer(self):
    return self._datum_writer

  @property
  def buffer_encoder(self):
    return self._buffer_encoder

  @property
  def sync_marker(self):
    return self._sync_marker

  @property
  def meta(self):
    return self._meta

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    # Perform a close if there's no exception
    if type is None:
      self.close()

  @property
  def block_count(self):
    return self._block_count

```
<h3><i>GetMeta(self, key)</i></h3>

Returns the metadata associated with the key. It takes `key` as a parameter for which associated metadata is returned. 


```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
* - `key`
  - byte value
  - Key of the metadata to report the value of.
  
```

<h4>Code Example</h4>

```python
def GetMeta(self, key):
    return self._meta.get(key)
```
<h3><i>SetMeta(self, key, value)</i></h3>

Sets the metadata value for the given key. To set the metadata at the given `key`, pass the `value` that has to be mapped.

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
* - `key`
  - bytes
  - Key of the metadata to report the value of.
* - `value`
  - `bytes` or `string`
  - Value that needs to set at a particular `key` of the metadata. The value passed as `string` are automatically converted into `bytes`.
  
```

<h4>Code Example</h4>

```python
def SetMeta(self, key, value):
    if isinstance(value, str):
      value = value.encode('utf-8')
    assert isinstance(value, bytes), (
        'Invalid metadata value for key %r: %r' % (key, value))
    self._meta[key] = value
```
<h3><i>_WriteHeader(self)</i></h3>

Writes Avro data file header.

<h4>Code Example</h4>

```python
  def _WriteHeader(self):
    header = {
        'meta': self.meta,
        'sync': self.sync_marker,
    }
    logger.debug(
        'Writing Avro data file header:\n%s\nAvro header schema:\n%s',
        header, META_SCHEMA)
    self.datum_writer.write_data(META_SCHEMA, header, self.encoder)
    self._header_written = True
```
## Class DataFileReader

DataFileReader class reads the file written by `DataFileWriter`. The class contains the methods and constructors to initialize the reader to read a specific Avro file using the `datum_reader`.

<h3><i>__init__(self, reader,datum_reader)</i></h3>

Initializes a new data file reader. It takes two arguments, `reader` to open the file to read using the `datum_reader`.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `reader`
  -  bytes
  -  Open file to read data from.
* - `datum_reader`
  -  bytes
  -  Avro datum reader
  
```
<h4>Code Example</h4>

```python
def __init__(self, reader, datum_reader):
    self._reader = reader
    self._raw_decoder = avro_io.BinaryDecoder(reader)
    self._datum_decoder = None # Maybe reset at every block.
    self._datum_reader = datum_reader

    # read the header: magic, meta, sync
    self._read_header()

    # ensure codec is valid
    avro_codec_raw = self.GetMeta('avro.codec')
    if avro_codec_raw is None:
      self.codec = "null"
    else:
      self.codec = avro_codec_raw.decode('utf-8')
    if self.codec not in VALID_CODECS:
      raise DataFileException('Unknown codec: %s.' % self.codec)

    self._file_length = self._GetInputFileLength()

    # get ready to read
    self._block_count = 0
    self.datum_reader.writer_schema = (
        schema.Parse(self.GetMeta(SCHEMA_KEY).decode('utf-8')))

```

<h3><i>GetMeta(self, key)</i></h3>

Returns the metadata associated with the `key` passed to it. It takes `key` of the metadata as an argument. The value of the metadata is returned in `bytes`.

**Return type**: `bytes`

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
* - `key`
  - byte value
  - Key of the metadata.
  
```
<h4>Code Example</h4>

```python
def GetMeta(self, key):
    return self._meta.get(key)
```

<h3><i>SetMeta(self, key,value)</i></h3>

Sets the metadata value at a particular metadata `key`. Always pass the matadate `key` to set the `value` for it. 

**Return type**: `bytes`

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
* - `key`
  - bytes
  - Key of the metadata.
* - `value`
  - bytes or string
  - Metadata value to set as bytes.
   
```
<h4>Code Example</h4>

```python
def SetMeta(self, key, value):
    if isinstance(value, str):
      value = value.encode('utf-8')
    self._meta[key] = value
```

<h3><i>_GetInputFileLength(self)</i></h3>

Returns the length of the input file.

**Return type**: length in `bytes`

<h4>Code Example</h4>

```python
def _GetInputFileLength(self):
    current_pos = self.reader.tell()
    self.reader.seek(0, 2)
    file_length = self.reader.tell()
    self.reader.seek(current_pos)
    return file_length

```

```{seealso}

- [Avro DatumReader](http://localhost:8000/io.html#datumreader-and-datumwriter-class).
- [Avro Schema Python APIs](http://localhost:8000/schema.html)

  






