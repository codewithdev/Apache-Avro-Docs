```{toctree}
:caption: 'Introduction'
:maxdepth: 3
index.md
schema.md
io.md
datafile.md
```

# Avro Python API Documentation
Avro is a data serialization framework use to convert the data into compact binary format. Avro contains the data along with the schema for which the data has to be serialized or deserialized. With the combination of schema, Avro eliminates the efforts of modifying the scheme everytime the data is serialized or deserialized.
Avro specifies two serialization encodings:
- Binary Format
- JSON(JavaScript Object Notation) Format

Avro implements with dynamically types language such as Python when data serialization is required at the runtime. For more information, see [Avro Introduction](https://avro.apache.org/docs/current/).

## Avro Python Overview
Avro provides support for the Python library which implements parts of the [Avro Specification](https://avro.apache.org/docs/1.11.1/specification/_print/). The library includes the following functionality:
- A schema parser, which can parse Avro schema (written in JSON) into a Schema object.
- Encoders and decoders to encode data into Avro format and decode it back using primitive functions.
- Streams for storing and reading data, which Encoders and Decoders use.

# Schemas
Avro comes with schemas that is fast and reliable for when the serialization happens for the data. This also facilitates with dynamic, scripting languages, since the data is combined with its schema.
When Avro data is stored in a file, its schema travels with it, so that files can be processed easily. 

```{seealso}
For more information, see {doc}`schema`. 
```
Using Avro, you can create schemas that contains primitive and complex data types. See [Avro Data Types](https://avro.apache.org/docs/1.8.2/spec.html#schemas) for declaring a schema.

## Getting Started with Avro Python
To get started with Avro, you can follow the steps described in [Getting Started Guide](https://avro.apache.org/docs/1.11.1/getting-started-python/).




