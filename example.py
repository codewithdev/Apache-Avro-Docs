import avro.schema

from avro.datafile import DataFileReader, DataFileWriter

from avro.io import DatumReader, DatumWriter

# Parse the schema file

schema = avro.schema.Parse(open("example.avsc", "rb").read())

# Create a data file using DataFileWriter

dataFile = open("example.avro", "wb")

writer = DataFileWriter(dataFile, DatumWriter(), schema)

# Write data using DatumWriter

writer.append({"name": "John Doe", "employee_id": "345"})
writer.append({"name": "Tracy", "employee_id": "45"})

writer.close()