import os
import json

# Diccionari per traduir els noms dels atributs
atributo_traduccion = {
    "strength": "Fuerza",
    "dexterity": "Destreza",
    "constitution": "Constitución",
    "intelligence": "Inteligencia",
    "wisdom": "Sabiduría",
    "charisma": "Carisma"
}

# Carpeta on es troben els JSON
carpeta_razas = "razas"

# Recorre tots els fitxers dins de la carpeta
for archivo in os.listdir(carpeta_razas):
    if archivo.endswith(".json"):
        ruta_completa = os.path.join(carpeta_razas, archivo)

        # Llegeix el fitxer JSON
        with open(ruta_completa, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Canvia els noms dels atributs dins de "attributes"
        if "attributes" in data:
            data["attributes"] = {atributo_traduccion.get(k, k): v for k, v in data["attributes"].items()}

        # Guarda el fitxer modificat
        with open(ruta_completa, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

print("Traducció completada per a tots els fitxers JSON.")
