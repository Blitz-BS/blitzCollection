from jsonschema import validate
import json

with open('examples/address.example.json') as f:
    example = json.load(f)

with open('json_schema/address.schema.json') as f:
    schema = json.load(f)

validate(instance=example, schema=schema)