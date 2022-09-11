# Avro Schema

## Overview

Avro Schemas are created in JSON format, which is lightweight text-based data format. It is composed of primitive and complex data types. Learn more about, [Avro Specification for Schemas](https://avro.apache.org/docs/1.8.2/spec.html#schemas).

A sample schema <code>example.avsc</code> is created to serialize and deserialize the data given below:

**example.avsc**    
```angular2html

{  "namespace: "example.avro",
   "type" : "record",
   "name" : "Employee",
   "fields" : [
    { "name" : "name" , "type" : "string" },
      { "name" : "employee_id" , "type" : "int"}
   ]
}

```
## Record Description
<table>
<thead>
<tr>
	<th>Field</th>
				<th>Description</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td><code>namespace</code>&nbsp;</td>
				<td><strong>(Optional)</strong> Namespace which defines the full name of the schema.&nbsp;</td>
			</tr>
			<tr>
				<td><code>type</code>&nbsp;</td>
				<td><strong>(Required)</strong> Type of document. In general if the document type is "record", it must have fields and data types.&nbsp;</td>
			</tr>
			<tr>
				<td><code>name</code>&nbsp;</td>
				<td><strong>(Required)</strong>The name of the namespace under which all the object resides.&nbsp;</td>
			</tr>
		</tbody>
</table>

```{seealso}
For more information, see [Defining a Schema](https://avro.apache.org/docs/1.11.1/getting-started-python/#defining-a-schema).
```

As a next step, you can serialize and deserialize the `example.avsc` avro schema data file using the code snippet and running the `schema.py` file.

## Serializing and Deserializing 

The data in Avro is stored along with its schema. You can always read the serialized data without code generation in Python. Once you have [defined the schema](https://avro.apache.org/docs/1.11.1/getting-started-python/#defining-a-schema), you can <code>import</code> avro package and add the serialization and deserialization process using the <code>DataFileReader</code> library in Avro.

```{seealso}
[Getting Started with Avro(Python)](https://avro.apache.org/docs/1.11.1/getting-started-python/).
```

**schema.py**

```
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("example.avsc", "rb").read())

writer = DataFileWriter(open("example.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "employee_id": 256})
writer.append({"name": "Ben", "employee_id": 7})
writer.append({"name": "Emiley", "employee_id": 67})
writer.close()

reader = DataFileReader(open("example.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
```

Avro implements with Python to provide you fast and reliable, no-code generation serialization system. The Avro Python API uses the following classes and methods for serialization and deserialization of Avro Schemas. For serialization it is necessary to use python class/methods.

In our example, we have created `example.avsc` schema for employee users and serialized and deserialized the data that generates the output in `example.avro` file in a binary format. 
A simple python class that initializes the object of `EmployeeClass`:

```
class EmployeeClass:
    def __init__(self, emp_id):
        self.name = name
        self.emp_id = emp_id
```
Defining the instance of `EmployeeClass`:
```
employee_user = EmployeeClass(name='Ben', emp_id= 348)
```
You can invoke the methods within the `EmployeeClass` to define the schema.

# Reference API for Classes and Methods

<h3><i>__init__</i></h3>

Use `__init__` method to initializes a new Schema object. To initialize a new schema object, you need to pass two parameters, `type` and `other_props`. The schema object is initialized within abstract base class.

<h4>Parameter Description</h4>

``` {list-table}
:header-rows: 1
* - Name 
  - type
  - Description
  - Example
* - `type`
  - string
  -  Type of Schema to be initialized. Learn more about [data types in Avro](https://avro.apache.org/docs/1.8.2/spec.html#schemas).
  -  "record", "Enum", "Arrays", "Maps", "Union", "Fixed"
  
* - `other_props`
  -  dict
  -  Dictionary of additional properties of schema.(optional)
  -  This can be created using decorators. For example, "name", "fullname", etc.
```

<h4>Code Example</h4>

```python
class Schema(object, metaclass= Employee.EmployeeMeta):
  def __init__(self, type, other_props=None):
    if type not in VALID_TYPES:
      raise SchemaParseException('%r is not a valid Avro type.' % type)

```

Where `VALID_TYPES` is initialized as an immutable version of set object.

```python
VALID_TYPES = frozenset.union(
  PRIMITIVE_TYPES,
  NAMED_TYPES,
  [
    ARRAY,
    MAP,
    UNION,
    REQUEST,
    ERROR_UNION,
  ],
)
```

<h3><i>__dict__</i></h3>

Returns the schema object.

**Return type**: dictionary that contains mapped values.


<h3><i>@property</i></h3>

A decorator within the `Schema` class that defines the properties of schema as a map. The properties can be defined in a map object using dictionary(property-> value).

<h3><i>@property</i> name</h3>

Initialize to return the simple name of the schema.

**Return type**: String
<h4>Code Example</h4>

```python
 self._props = {}
 self._props['type'] = type
 self._type = type
 if other_props:
      self._props.update(other_props)

@property
def name(self):
    # Return the simple name of the schema. By default the full name of schema is the simple name.
    return self._props['name']
```
<h3><i>@property</i> fullname</h3>

Initialize to return the full name of the schema. 

**Return type**: String
<h4>Code Example</h4>

```python
@property
def fullname(self):
    return self.name

```
<h3><i>@property</i> namespace</h3>

Defines the function to describes the name of the namespace to which the schema object belongs. By default, if there is no namespace is found for the schema it returns `None`. It is used to differentiate one schema type from another should they share the same name.

**Return type:** String
<h4>Code Example</h4>

```python
@property
def namespace(self):
    return self._props.get('namespace', None)

```

<h3><i>@property</i> type</h3>
Defines the type of the schema. This comes under the document as well as under the field name. It returns the type of the schema.

**Return Type:** String
<h4>Code Example</h4>


```python
@property
  def type(self):
    return self._type
```

<h3><i>@property</i> props</h3>

Returns the dictionary containing all properties associated with schema generated from dict that contains reserved and non-reserved properties.

**Return type**: dictionary

<h4>Code Example</h4>

```python
def props(self):
    return ImmutableDict(self._props)
```

<h3><i>@property</i> other_props</h3>

Returns the dictionary of all non-reserved properties associated with schema.

**Return type**: dictionary

<h4>Code Example</h4>

```python
  @property
  def other_props(self):
    return dict(FilterKeysOut(items=self._props, keys=SCHEMA_RESERVED_PROPS))
```
<h3><i>__str__</i></h3>
Define this method to return the JSON representation of the schema. 

**Return type**: readable JSON output

<h4>Code Example</h4>

```python
 def __str__(self):
    return json.dumps(self.to_json())
```
<h3><i>to_json(self, names)</i></h3>

Converts the schema object into [AVRO specification representation](https://avro.apache.org/docs/1.8.2/spec.html#schemas). The function takes `name` of schema type as a parameter to convert a specific type of schema that have names in it. For example, "record", "enum", and "fixed". This can be passed within the abstract class of the schema definition.

<h4>Code Example</h4>

```python
 @abc.abstractmethod
  def to_json(self, names):
    raise Exception('Cannot run abstract method.')
```

##### Class Name(object)
Defines class to represent the Avro name.

<h3><i>__init(name, namespace=None)</i></h3>
Initializes object to parse an Avro name. It takes two arguments, `name` and `namespace`.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
  - Example
 
* - `name`
  - `string`
  - Name of the Avro schema which has to be parse. It can be relative or absolute.
  - "Example-employee"
* - `namespace`
  - `string`
  - ` (Optional)` Add namespace if the `name` is relative. If the `name` is absolute, this can be ignored.
  - "Example-namespace"
  
```
<h4>Code Example</h4>

```python
class Name(object):
  def __init__(self, name, namespace=None):
    if namespace is None: namespace = ''

    if '.' in name:
      # name is absolute, namespace is ignored:
      self._fullname = name

      match = _RE_FULL_NAME.match(self._fullname)
      if match is None:
        raise SchemaParseException(
            'Invalid absolute schema name: %r.' % self._fullname)

      self._name = match.group(1)
      self._namespace = self._fullname[:-(len(self._name) + 1)]

    else:
      # If name is relative, combine with explicit namespace:
      self._name = name
      self._namespace = namespace
      self._fullname = '%s.%s' % (self._namespace, self._name)

      # Validate the fullname:
      if _RE_FULL_NAME.match(self._fullname) is None:
        raise SchemaParseException(
            'Invalid schema name %r infered from name %r and namespace %r.'
            % (self._fullname, self._name, self._namespace))

```
<h3><i>@property</i> simple_name</h3>

Returns the simple name of the Avro schema.

**Return type**: String

<h4>Code Example</h4>

```python
@property
  def simple_name(self):
    return self._name
```
<h3><i>@property</i> namespace</h3>

Returns the parsed Avro name's namespace. It can be possibly an empty string.

**Return type**: String

<h4>Code Example</h4>

Converts the schema object into [AVRO specification representation](https://avro.apache.org/docs/1.8.2/spec.html#schemas). The function takes `name` of schema type as a parameter to convert a specific type of schema that have names in it. For example, "record", "enum", and "fixed". This can be passed within the abstract class of the schema definition.

<h4>Code Example</h4>

```python
@property
  def namespace(self):
    return self._namespace

```

<h3><i>@property</i> fullname</h3>

Returns the parsed Avro name's fullname. It always returns a string with period(.).

**Return type**: String

<h4>Code Example</h4>

```python
 @property
  def fullname(self):
    return self._fullname
```
##### Class Names(object)
This class tracks the named schema of Avro and default namespace during parsing of Avro schema. 
To track Avro schemas that has defined [Avro named schemas](schema.html#class-name-object) and default namespace, you can initialize the class. It returns the name of Avro named schema.

<h3><i>__init__(default_namespace=None, names=None)</i></h3>

Initializes a new name tracker. It takes two parameters, `default_namespace` and `names` that provision the tracker to create new namespace.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `default_namespace`
  - `string`
  - (Optional) Default namespace."
* - `names`
  - `string`
  - ` (Optional)` Initial mapping of known named schemas.
  
```

```python
class Names(object):
  def __init__(self, default_namespace=None, names=None):
    if names is None:
      names = {}
    self._names = names
    self._default_namespace = default_namespace
```
<h3><i>@property</i> names</h3>

Returns the mapping of known named schema.

**Return type**: String

<h4>Code Example</h4>

```python
 @property
  def names(self):
    return self._names
```
<h3><i>@property</i> default_namespace</h3>

Returns the default namespace(if any). By default it returns `None` if there is no default namespace is defined.

**Return type**: String

<h4>Code Example</h4>

```python
 @property
  def default_namespace(self):
    return self._default_namespace
```
<h3><i>NewWithDefaultNamespace(namespace)</i></h3>

Creates a new tracker with a new default namespace. It overrides the default namespace which has been defined already. It takes `namespace` as an argument.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `namespace`
  - `string`
  - (Required) New name of the default namespace."
  
```

**Return type**: String

<h4>Code Example</h4>

```python
 def NewWithDefaultNamespace(self, namespace):
    return Names(names=self._names, default_namespace=namespace)
```

<h3><i>GetName(name, namespace=None)</i></h3>

Updates the Avro name according to the tracker's namespace. It takes two arguments, `name` that has to be resolved and an optional `namespace`.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `name`
  - `string`
  - (Required) Name to resolve. It can be absolute or relative."

* - `namespace`
  - `string`
  - (Optional) Explicit namespace. If the `name` is absolute, this can be ignored. However, if `name` is relative, mention the namespace as well.
  
```

**Return type**: String

<h4>Code Example</h4>

```python
def GetName(self, name, namespace=None):
    if namespace is None: namespace = self._default_namespace
    return Name(name=name, namespace=namespace)
```

<h3><i>GetSchema(name, namespace=None)</i></h3>

Updates Avro Schema by name. It takes two parameters, `name` of the Avro schema to lookup and `namespace` of the Avro schema.

**Return type**: Schema object with specified name, if any. By default it returns `NONE`.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `name`
  - `string`
  - (Required) Name of the Avro Schema."

* - `namespace`
  - `string`
  - (Optional) Explicit namespace. If the `name` is absolute, this can be ignored. However, if `name` is relative, mention the namespace as well.
  
```
<h4>Code Example</h4>

```python

 def GetSchema(self, name, namespace=None):
    avro_name = self.GetName(name=name, namespace=namespace)
    return self._names.get(avro_name.fullname, None)
```

##### Class NamedSchema(Schema)

This class is the abstract base class of the named Avro Schema. Named Avro Schemas are enumerated by `NAMED_TYPES`. For more information, see [Complex Types in Avro](https://avro.apache.org/docs/1.9.1/spec.html#schema_complex).

Where `NAMED_TYPES` is defined as,

```python
NAMED_TYPES = frozenset([
  FIXED,
  ENUM,
  RECORD,
])
```

<h3><i>__init__(type, name, namespace=None, names=None, other_props=None)</i></h3>

Initializes a new named Schema object with properties that contains `name`,`type`, `namespace`, `names`, and additional properties `other_props` associated with the Schema.

<h4>Parameter Description</h4>

``` {list-table}
:header-rows: 1
* - Name 
  - type
  - Description
* - `name`
  -  string
  -  Name of the Avro Schema. It can be absolute or relative.

* - `type`
  -  string 
  - Type of the Avro named Schema. For example, "record", "Enum", "Arrays", "Maps", "Union", "Fixed".
  
* - `other_props`
  -  dict
  -  Dictionary of additional properties of schema.(optional)
* - `names`
  - string
  - Tracker to resolve and register the avro name.

```
<h4>Code Example</h4>

```python
def __init__(
      self,
      type,
      name,
      namespace=None,
      names=None,
      other_props=None,
  ):
    assert (type in NAMED_TYPES), ('Invalid named type: %r' % type)
    self._avro_name = names.GetName(name=name, namespace=namespace)

    super(NamedSchema, self).__init__(type, other_props)

    names.Register(self)

    self._props['name'] = self.name
    if self.namespace:
      self._props['namespace'] = self.namespace

```
<h3><i>GetSchema(name, namespace=None)</i></h3>

Updates Avro Schema by name. It takes two parameters, `name` of the Avro schema to lookup and `namespace` of the Avro schema.

**Return type**: Schema object with specified name, if any. By default it returns `NONE`.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `name`
  - `string`
  - (Required) Name of the Avro Schema."

* - `namespace`
  - `string`
  - (Optional) Explicit namespace. If the `name` is absolute, this can be ignored. However, if `name` is relative, mention the namespace as well.
  
```
<h4>Code Example</h4>

```python
def GetSchema(self, name, namespace=None):
    avro_name = self.GetName(name=name, namespace=namespace)
    return self._names.get(avro_name.fullname, None)

```

#### Class Field(object)

The field holds a JSON array containing the list of fields in the schema, each having name and its type attributes. In general, if the schema type is "record" or any document, it can have multiple fields having values and properties defined in it. 

**Example**: A record containing the field `Employee` must have `name` and `age` of the employee.

```json
{
   "type" : "record",
   "namespace" : "Avro Docs",
   "name" : "Employee",
   "fields" : [
      { "name" : "Name" , "type" : "string" },
      { "name" : "Age" , "type" : "int" }
   ]
}
```
<h3><i>__init__(type, name, index, names=None, doc= None,other_props=None)</i></h3>

The method initializes a schema of a field in a record. To initialize the field, it takes `name`, `type`, `index`, `names`, `doc`, `other_props` as a parameter.

<h4>Parameter Description</h4>

```{list-table}
:header-rows: 1

* - Parameter
  - type
  - Description
 
* - `name`
  - `string`
  - (Required) Name of the field."

* - `type`
  - `string`
  - Avro schema of the field. For example, "record".
  
* - `index`
  - int
  - Index of the field starting from 0.
  
* - `names`
  - string
  - Avro named schema's namespace.
* - doc
  - Describes the name of the field. In case of document, it refers to the schema name.  

```

<h4>Code Example</h4>

```python
class Field(object):
    def __init__(
      self,
      type,
      name,
      index,
      has_default,
      default=_NO_DEFAULT,
      order=None,
      names=None,
      doc=None,
      other_props=None
  ):
    if (not isinstance(name, str)) or (len(name) == 0):
      raise SchemaParseException('Invalid record field name: %r.' % name)
    if (order is not None) and (order not in VALID_FIELD_SORT_ORDERS):
      raise SchemaParseException('Invalid record field order: %r.' % order)

    # All properties of this record field:
    self._props = {}

    self._has_default = has_default
    if other_props:
      self._props.update(other_props)

    self._index = index
    self._type = self._props['type'] = type
    self._name = self._props['name'] = name

    if order is not None:
      self._props['order'] = order

    if doc is not None:
      self._props['doc'] = doc
```





```python

class Field(object):
  """Representation of the schema of a field in a record."""

  def __init__(
      self,
      type,
      name,
      index,
      has_default,
      default=_NO_DEFAULT,
      order=None,
      names=None,
      doc=None,
      other_props=None
  ):
    """Initializes a new Field object.
    Args:
      type: Avro schema of the field.
      name: Name of the field.
      index: 0-based position of the field.
      has_default:
      default:
      order:
      names:
      doc:
      other_props:
    """
    if (not isinstance(name, str)) or (len(name) == 0):
      raise SchemaParseException('Invalid record field name: %r.' % name)
    if (order is not None) and (order not in VALID_FIELD_SORT_ORDERS):
      raise SchemaParseException('Invalid record field order: %r.' % order)

    # All properties of this record field:
    self._props = {}

    self._has_default = has_default
    if other_props:
      self._props.update(other_props)

    self._index = index
    self._type = self._props['type'] = type
    self._name = self._props['name'] = name

    # TODO: check to ensure default is valid
    if has_default:
      self._props['default'] = default

    if order is not None:
      self._props['order'] = order

    if doc is not None:
      self._props['doc'] = doc
```
<h3><i>@property</i> type</h3>

Returns the schema of the field.

**Return type**: String

<h4>Code Example</h4>

```python
 @property
  def type(self):
    return self._type
```
<h3><i>to_json(names)</i></h3>

Returns the JSON string that has been converted from schema object. It takes Avro named schema `names` as a parameter to conver the schema object to JSON string.

**Return type**: String

<h4>Code Example</h4>

```python
 def to_json(self, names=None):
    if names is None:
      names = Names()
    to_dump = self.props.copy()
    to_dump['type'] = self.type.to_json(names)
    return to_dump

```

## Module Functions

<h3><i>Parse(json_string)</i></h3>

Builds a schema from its JSON descriptor in readonly text form. The function takes `json_string` as an argument that returns a parsed Avro schema. When it is unable to parse the `json_string` that it has taken, it raises `SchemaParseException`.

**Return type**: string. If not parsed correctly, it throws an Parse Exception error.

<h4>Code Example</h4>

```python
def Parse(json_string):
  try:
    json_data = json.loads(json_string)
  except Exception as exn:
    raise SchemaParseException(
        'Error parsing schema from JSON: %r. '
        'Error message: %r.'
        % (json_string, exn))

  # Initialize the names object
  names = Names()

  # construct the Avro Schema object
  return SchemaFromJSONData(json_data, names)
```
## Avro Exceptions for Schema

<h3><i>SchemaParseException(AvroException)</i></h3>

SchemaParseException are throws while parsing Avro schema description. This can be implemented in any class such as `Name` and `Schema` class where Avro properties are mapped. 

<h4>Code Example</h4>

```python
class SchemaParseException(AvroException):
  pass

class Schema(object, metaclass=abc.ABCMeta):
  # Abstract base class for all Schema classes.

  def __init__(self, type, other_props=None):
    # Initializes a new schema object.
    if type not in VALID_TYPES:
      raise SchemaParseException('%r is not a valid Avro type.' % type)

```


```{seealso} 
- [Avro Specification for Schema and Data Types](https://avro.apache.org/docs/1.8.2/spec.html#schemas).
```

```{tip}
If you have [installed the Avro Python package](https://avro.apache.org/docs/1.11.1/getting-started-python/), you can quickly get started by importing the `avro` package in your code. A working example is given in the file below:

```

```python
import copy
import json
import avro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader

schema = {
    'name': 'avro.example.User',
    'type': 'record',
    'fields': [
        {'name': 'name', 'type': 'string'},
        {'name': 'age', 'type': 'int'}
    ]
}

# Parse the schema so we can use it to write the data
schema_parsed = avro.schema.Parse(json.dumps(schema))

# Write data to an avro file
with open('users.avro', 'wb') as f:
    writer = DataFileWriter(f, DatumWriter(), schema_parsed)
    writer.append({'name': 'John Doe', 'age': 77})
    writer.append({'name': 'Tracy', 'age': 53})
    writer.close()

# Read data from an avro file
with open('users.avro', 'rb') as f:
    reader = DataFileReader(f, DatumReader())
    metadata = copy.deepcopy(reader.meta)
    schema_from_file = json.loads(metadata['avro.schema'])
    users = [user for user in reader]
    reader.close()

print(f'Schema that we specified:\n {schema}')
print(f'Schema that we parsed:\n {schema_parsed}')
print(f'Schema from users.avro file:\n {schema_from_file}')
print(f'Users:\n {users}')

# Schema that we specified:
#  {'name': 'avro.example.User', 'type': 'record',
#   'fields': [{'name': 'name', 'type': 'string'}, {'name': 'age', 'type': 'int'}]}
# Schema that we parsed:
#  {"type": "record", "name": "User", "namespace": "avro.example",
#   "fields": [{"type": "string", "name": "name"}, {"type": "int", "name": "age"}]}
# Schema from users.avro file:
#  {'type': 'record', 'name': 'User', 'namespace': 'avro.example',
#   'fields': [{'type': 'string', 'name': 'name'}, {'type': 'int', 'name': 'age'}]}
# Users:
#  [{'name': 'Pierre-Simon Laplace', 'age': 77}, {'name': 'John von Neumann', 'age': 53}]

```






