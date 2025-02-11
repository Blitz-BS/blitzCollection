"""
Ce script valide des fichiers JSON dans le répertoire "examples" en utilisant les schémas JSON spécifiés dans chaque fichier.
"""
import json
import requests
from jsonschema import validate
from os import listdir  

for file in listdir('examples'):
    with open(f'examples/{file}', encoding='utf-8') as f:
        example = json.load(f)
    if '$schema' in example:
        resp = requests.get(url=example['$schema'])
        schema = resp.json()
        #with open(f"json_schema/{file.split(".")[0]}.schema.json", encoding='utf-8') as f_schema:
            #schema = json.load(f_schema)
        validate(instance=example, schema=schema)
        print(f"le fichier {file} est valide")
    else:
        raise Exception(f"le fichier {file} ne précise pas de schéma")