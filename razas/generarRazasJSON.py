import os
import json

# Lista de nombres de archivos JSON a generar
json_files = [
    "humanos.json", "semihumanos.json", "draconidos.json", "kobolds.json", "elfos.json", "enanos.json", 
    "gnomos.json", "medianos.json", "semiorcos.json", "tieflings.json", "goblins.json", "slimes.json", 
    "tabaxis.json", "locahtah.json", "throthogas.json", "loxodon.json", "centauro.json", "vedalken.json", 
    "forjados.json", "githyanki.json", "aasimar.json", "kenkus.json", "ursoi.json", "yuhan-ti.json", 
    "lamia.json", "grung.json", "sucubo-incubo.json", "harengon.json", "shura.json", "pixie.json", 
    "no-muerto.json", "kitsune.json", "drow.json", "foxfolks.json", "druegar.json", "owlers.json", 
    "efteros.json", "genasi.json", "hobgoblins.json", "wolven.json", "lizerins.json", "firbolgs.json", 
    "goliats.json", "vanaras.json", "minotauros.json", "sonares.json", "insectoides.json", "miconidos.json", 
    "PSOE.json"
]

# Plantilla para el contenido del archivo JSON
def create_json_content(file_name):
    return {
        "raceName": file_name.replace(".json", ""),
        "raceDescription": "",
        "bonusRules": "",
        "movementSpeed": "",
        "lifeSpan": "",
        "attributes": {
            "strength": "0",
            "dexterity": "0",
            "constitution": "0",
            "intelligence": "0",
            "wisdom": "0",
            "charisma": "0"
        },
        "sizes": [],
        "abilities": []
    }

# Crear archivos JSON
for file_name in json_files:
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(create_json_content(file_name), file, indent=4, ensure_ascii=False)
        print(f"Archivo creado: {file_name}")
    else:
        print(f"Archivo ya existe: {file_name}")
