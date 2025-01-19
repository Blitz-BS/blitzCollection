"""
Ce script valide des fichiers JSON dans le répertoire "examples" en utilisant les schémas JSON spécifiés dans chaque fichier.
"""
from jsonschema import validate
import json
from os import listdir
import requests

for file in listdir('examples'):
    with open(f'examples/{file}') as f:
        example = json.load(f)
    if '$schema' in example:
        resp = requests.get(url=example['$schema'])
        schema = resp.json()
        validate(instance=example, schema=schema)
        print(f"le fichier {file} est valide")
    else:
        raise Exception(f"le fichier {file} ne précise pas de schéma") 