import os
import json

# Carpeta on es troben els arxius JSON
folder_path = "razas"

# Recorre tots els fitxers de la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # Llegeix el fitxer JSON
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Elimina les entrades amb valor "0" dins de 'attributes'
        if "attributes" in data and isinstance(data["attributes"], dict):
            data["attributes"] = {k: v for k, v in data["attributes"].items() if v != "0"}

        # Guarda els canvis al mateix fitxer
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

print("Processament complet.")
