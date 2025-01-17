"""
Ce script vérifie si les fichiers `example.json` du répertoire `examples` sont valides par rapport aux fichiers `schema.json` du répertoire `json_schema`.
"""

from jsonschema import validate
import json
from os import listdir

for file in listdir('examples'):
    if "example.json" in file:
        object_name = file.split('.example.json')[0]
        
        with open(f'examples/{object_name}.example.json') as f:
            example = json.load(f)

        with open(f'json_schema/{object_name}.schema.json') as f:
            schema = json.load(f)

        validate(instance=example, schema=schema)
        print(f"le fichier {file} est valide")
    else:
        raise Exception(f"ce fichier {file} n'est pas un fichier example.json") 