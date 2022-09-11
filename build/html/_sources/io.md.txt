
# Input and Output Utilities

## Overview
Avro provides a convenient way to represent complex data structures within schema. Avro data can be used as both input to and output, as well as the intermediate format. The Input and Output utilities includes APIs to validate schema and generic representation of the data for which schema attributes are implemented using `dict` data type.
The Input and Output utilities involves set of APIs, classes, and methods that are used in serialization and deserialization of Avro schemas.

The set of classes and methods implements DatumReader and DatumWriter interface to read encoded Avro schemas.

```{seealso}

[Avro Schema Specificiation](https://avro.apache.org/docs/1.10.2/spec.html#schema_complex)

```

## Validating Avro Schema

<h3><i>Validate(expected_schema, datum)</i></h3>

The function implements the validation process to check if the python datum is an instance of Avro schema. It takes two parameters `expected_schema` and `datum` to validate.

**Return type**: `boolean`. `True` if datum is an instance of schema.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `expected_schema`
  - It can be `null`, `boolean`, `string`, `bytes`, `int`. See, [schema data types](https://avro.apache.org/docs/1.10.2/spec.html#schema_complex).
  - Schema to validate against.
* - `datum`
  - `map`
  - Datum to validate.
  
```
<h4>Code Example</h4>

```python
def Validate(expected_schema, datum):
  schema_type = expected_schema.type
  if schema_type == 'null':
    return datum is None
  elif schema_type == 'boolean':
    return isinstance(datum, bool)
  elif schema_type == 'string':
    return isinstance(datum, str)
  elif schema_type == 'bytes':
    return isinstance(datum, bytes)
  elif schema_type == 'int':
    return (isinstance(datum, int)
        and (INT_MIN_VALUE <= datum <= INT_MAX_VALUE))
  elif schema_type == 'long':
    return (isinstance(datum, int)
        and (LONG_MIN_VALUE <= datum <= LONG_MAX_VALUE))
  elif schema_type in ['float', 'double']:
    return (isinstance(datum, int) or isinstance(datum, float))
  elif schema_type == 'fixed':
    return isinstance(datum, bytes) and (len(datum) == expected_schema.size)
  elif schema_type == 'enum':
    return datum in expected_schema.symbols
  elif schema_type == 'array':
    return (isinstance(datum, list)
        and all(Validate(expected_schema.items, item) for item in datum))
  elif schema_type == 'map':
    return (isinstance(datum, dict)
        and all(isinstance(key, str) for key in datum.keys())
        and all(Validate(expected_schema.values, value)
                for value in datum.values()))
  elif schema_type in ['union', 'error_union']:
    return any(Validate(union_branch, datum)
               for union_branch in expected_schema.schemas)
  elif schema_type in ['record', 'error', 'request']:
    if not isinstance(datum, dict):
        return False
    expected_schema_field_names = set()
    for field in expected_schema.fields:
        expected_schema_field_names.add(field.name)
        if not Validate(field.type, datum.get(field.name)):
            return False
    for datum_field in datum.keys():
        if datum_field not in expected_schema_field_names:
            return False
    return True
  else:
    raise AvroTypeException('Unknown Avro schema type: %r' % schema_type)
```

## Datum Validation Exceptions

<h3 style="color:red;"><i>AvroTypeException</i></h3>

This exception is raised when datum is not an instance of schema. 

<h4>Code Example</h4>

```python
class AvroTypeException(schema.AvroException):
  def __init__(self, expected_schema, datum):
    pretty_expected = json.dumps(json.loads(str(expected_schema)), indent=2)
    fail_msg = "The datum %s is not an example of the schema %s"\
               % (datum, pretty_expected)
    schema.AvroException.__init__(self, fail_msg)

```
## Decoder and Encoder Class

Python API implements decoder and encoder class to read and write leaf values of Avro schema. This class supports methods that reads Avro values (`read_utf8()`, `read_long()`,and bytes). It also support reading `int`, `boolean`, `map`, and `arrays`. The decoder class contains Decoder constructors and configurations utilities.

<h3><i>BinaryDecoder(object)</i></h3>

Decoder Class contains methods and constructors to read leaf values. It also initializes reader python object that help decoder to read Avro values.

<h4>Code Example</h4>

```python
class BinaryDecoder(object):
  def __init__(self, reader):
    self._reader = reader

```

<h3><i>@property</i> reader(self)</h3>

Reader object used by Decoder to read Avro values.

**Return type**: Python object

<h4>Code Example</h4>

```python
 @property
  def reader(self):
    return self._reader
```

<h3><i>@property</i> reader(self,n)</h3>

Decoder uses reader object to read n bytes. It takes one argument `n` that specifies the number of bytes to read.

**Return type**: n bytes from the input.

<h4>Code Example</h4>

```python
def read(self, n):
    assert (n >= 0), n
    input_bytes = self.reader.read(n)
    assert (len(input_bytes) == n), input_bytes
    return input_bytes
```
<h3><i>@property</i> read_utf8(self)</h3>

Reads the string encoded as a `long` followed by the bytes of UTF-8 encoded characters.

<h4>Code Example</h4>

```python
def read_utf8(self):
    input_bytes = self.read_bytes()
    try:
      return input_bytes.decode('utf-8')
    except UnicodeDecodeError as exn:
      logger.error('Invalid UTF-8 input bytes: %r', input_bytes)
      raise exn
```

<h3><i>read_bytes(self)</i></h3>

Reads a byte string. If there is no bytes, it returns null.

**Return type**: bytes

<h4>Code Example</h4>

```python
def read_bytes(self):
    nbytes = self.read_long()
    assert (nbytes >= 0), nbytes
    return self.read(nbytes)
```

<h3><i>read_long(self)</i></h3>

Reads a long written by `write_long(self,datum)`.

**Return type**: 

<h4>Code Example</h4>

```python
def read_long(self):
    b = ord(self.read(1))
    n = b & 0x7F
    shift = 7
    while (b & 0x80) != 0:
      b = ord(self.read(1))
      n |= (b & 0x7F) << shift
      shift += 7
    datum = (n >> 1) ^ -(n & 1)
    return datum
```
<h3><i>BinaryEncoder(object)</i></h3>

Encoder Class contains methods and constructors to write leaf values. It also initializes writer python object that help encode the `int`, `booloean`, and [other complex types](https://avro.apache.org/docs/1.10.2/spec.html#schema_complex) of Avro schema. The Encoder class uses writer python object to write a sequence of bytes.

<h4>Code Example</h4>

```python
class BinaryEncoder(object):
  def __init__(self, writer):
    self._writer = writer
```
<h3><i>@property</i> writer(self)</h3>

Writer object use to encode values.

<h4>Code Example</h4>

```python
 @property
  def writer(self):
    return self._writer
```
<h3><i>write(self, datum)</i></h3>

Writes a sequence of bytes. It takes datum; Byte array that needs to be encoded.

<h4>Code Example</h4>

```python
def write(self, datum):
    assert isinstance(datum, bytes), ('Expecting bytes, got %r' % datum)
    self.writer.write(datum)
```
<h3><i>write_int(self, datum)</i></h3>

Writes 32-bit int and long values. It takes `datum` as an argument which has to be encoded.

<h4>Code Example</h4>

```python
def write_int(self, datum):
    self.write_long(datum);
```
<h3><i>write_bytes(self, datum)</i></h3>

Write a byte string. It takes `datum` as an argument which has to be encoded.

<h4>Code Example</h4>

```python
def write_bytes(self, datum):
    self.write_long(len(datum))
    self.write(datum)

```

<h3><i>write_utf8(self, datum)</i></h3>

Writes a UTF-8 encoded string. It takes `datum` as an argument which has to be encoded.

<h4>Code Example</h4>

```python
def write_utf8(self, datum):
    datum = datum.encode("utf-8")
    self.write_bytes(datum)
```

## DatumReader and DatumWriter Class

<h3><i>DatumReader(object)</i></h3>

The class represents the DatumReader interface which deserializes Avro-encoded data into a Python data structures. To validate the schema properly, multiple class level static method bound to DatumReader class.

**Return type**: `boolean`

<h4>Code Example</h4>

```python
class DatumReader(object):
  @staticmethod
  def check_props(schema_one, schema_two, prop_list):
    for prop in prop_list:
      if getattr(schema_one, prop) != getattr(schema_two, prop):
        return False
    return True
```
<h3><i>@staticmethod</i>match_schema</h3>

Returns True if input schema matches with the output schema.

**Return type**: `boolean`

<h4>Code Example</h4>

```python
@staticmethod
  def match_schemas(writer_schema, reader_schema):
    w_type = writer_schema.type
    r_type = reader_schema.type
    if 'union' in [w_type, r_type] or 'error_union' in [w_type, r_type]:
      return True
    elif (w_type in schema.PRIMITIVE_TYPES and r_type in schema.PRIMITIVE_TYPES
          and w_type == r_type):
      return True
    elif (w_type == r_type == 'record' and
          DatumReader.check_props(writer_schema, reader_schema,
                                  ['fullname'])):
      return True
    elif (w_type == r_type == 'error' and
          DatumReader.check_props(writer_schema, reader_schema,
                                  ['fullname'])):
      return True
    elif (w_type == r_type == 'request'):
      return True
    elif (w_type == r_type == 'fixed' and
          DatumReader.check_props(writer_schema, reader_schema,
                                  ['fullname', 'size'])):
      return True
    elif (w_type == r_type == 'enum' and
          DatumReader.check_props(writer_schema, reader_schema,
                                  ['fullname'])):
      return True
    elif (w_type == r_type == 'map' and
          DatumReader.check_props(writer_schema.values,
                                  reader_schema.values, ['type'])):
      return True
    elif (w_type == r_type == 'array' and
          DatumReader.check_props(writer_schema.items,
                                  reader_schema.items, ['type'])):
      return True
```
<h3><i>__init__(self,writer_schema=None, reader_schema=None)</i></h3>

As defined in the Avro specification, we call the schema encoded  in the "writer's schema", and the schema expected by the "reader's schema". A `set_writer_schema` and `set_reader_schema` is defined to read and write the properties of the schema.

**Return type**: Schema object

<h4>Code Example</h4>

```python
def __init__(self, writer_schema=None, reader_schema=None):
    self._writer_schema = writer_schema
    self._reader_schema = reader_schema

  # read/write properties
  def set_writer_schema(self, writer_schema):
    self._writer_schema = writer_schema
  writer_schema = property(lambda self: self._writer_schema,
                            set_writer_schema)
  def set_reader_schema(self, reader_schema):
    self._reader_schema = reader_schema
  reader_schema = property(lambda self: self._reader_schema,
                            set_reader_schema)

  def read(self, decoder):
    if self.reader_schema is None:
      self.reader_schema = self.writer_schema
    return self.read_data(self.writer_schema, self.reader_schema, decoder)

```
<h3><i>read_data(self,writer_schema,reader_schema,decoder)</i></h3>

The function uses the decoder to convert the schema datum into python data structures and matches with the `reader_schema`. This help validate the schema.

<h4>Code Example</h4>

```python
def read_data(self, writer_schema, reader_schema, decoder):
    # schema matching
    if not DatumReader.match_schemas(writer_schema, reader_schema):
      fail_msg = 'Schemas do not match.'
      raise SchemaResolutionException(fail_msg, writer_schema, reader_schema)
```
<h3 style="color:red;"><i>SchemaResolutionException</i></h3>

The exception are raised when schema doesn't matches after validation.  

<h4>Code Example</h4>

```python
  def __init__(self, fail_msg, writer_schema=None, reader_schema=None):
    pretty_writers = json.dumps(json.loads(str(writer_schema)), indent=2)
    pretty_readers = json.dumps(json.loads(str(reader_schema)), indent=2)
    if writer_schema: fail_msg += "\nWriter's Schema: %s" % pretty_writers
    if reader_schema: fail_msg += "\nReader's Schema: %s" % pretty_readers
    schema.AvroException.__init__(self, fail_msg)
```

<h3><i>DatumWriter(object)</i></h3>

The class represents the DatumWriter interface which serializes Avro-encoded data into generic Python data object. The read and write utility functions can be defined within the DatumWriter class to validate the properties of the schema.

<h4>Code Example</h4>

```python
class DatumWriter(object):
  def __init__(self, writer_schema=None):
    self._writer_schema = writer_schema

```

<h3><i>set_writer_schema(self, writer_schema)</i></h3>

The function defines write properties of the schema.

<h4>Code Example</h4>

```python
 def set_writer_schema(self, writer_schema):
    self._writer_schema = writer_schema
  writer_schema = property(lambda self: self._writer_
                           def write(self, datum, encoder):
    # Validating datum
    if not Validate(self.writer_schema, datum):
      raise AvroTypeException(self.writer_schema, datum)

    self.write_data(self.writer_schema, datum, encoder)

```
<h3><i>write_data(self, writer_schema, datum, encoder)</i></h3>

The function encoded the writer schema to python data objects. Once the datum is encoded, it can be further decoded to match with the `writer_schema` for validation.

<h4>Code Example</h4>

```python
def write_data(self, writer_schema, datum, encoder):
    # function dispatch to write datum
    if writer_schema.type == 'null':
      encoder.write_null(datum)
    elif writer_schema.type == 'boolean':
      encoder.write_boolean(datum)
    elif writer_schema.type == 'string':
      encoder.write_utf8(datum)
    elif writer_schema.type == 'int':
      encoder.write_int(datum)
    elif writer_schema.type == 'long':
      encoder.write_long(datum)
    elif writer_schema.type == 'float':
      encoder.write_float(datum)
    elif writer_schema.type == 'double':
      encoder.write_double(datum)
    elif writer_schema.type == 'bytes':
      encoder.write_bytes(datum)
    elif writer_schema.type == 'fixed':
      self.write_fixed(writer_schema, datum, encoder)
    elif writer_schema.type == 'enum':
      self.write_enum(writer_schema, datum, encoder)
    elif writer_schema.type == 'array':
      self.write_array(writer_schema, datum, encoder)
    elif writer_schema.type == 'map':
      self.write_map(writer_schema, datum, encoder)
    elif writer_schema.type in ['union', 'error_union']:
      self.write_union(writer_schema, datum, encoder)
    elif writer_schema.type in ['record', 'error', 'request']:
      self.write_record(writer_schema, datum, encoder)
    else:
      fail_msg = 'Unknown type: %s' % writer_schema.type
      raise schema.AvroException(fail_msg)

```


```{seealso}

[Avro Schema Python APIs](/schema.html)

```














