"""
Ce script vérifie si les fichiers `example.json` du répertoire `examples` sont valides par rapport aux fichiers `schema.json` du répertoire `json_schema`.
"""
from jsonschema import validate
import json
from os import listdir
import requests

object_name = 'address'

with open(f'examples/{object_name}.example.json') as f:
    example = json.load(f)

resp = requests.get(url=example['$schema'])
schema = resp.json()

validate(instance=example, schema=schema)