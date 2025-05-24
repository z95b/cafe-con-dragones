import requests
import csv

# URL base de la API
BASE_URL = "https://www.dnd5eapi.co/api/spells"

# Realizar la solicitud a la API para obtener la lista de conjuros
response = requests.get(BASE_URL)
if response.status_code != 200:
    print("Error al acceder a la API:", response.status_code)
    exit()

# Obtener los resultados de la API
spells = response.json().get("results", [])

# Lista para almacenar los datos detallados de los conjuros
spell_data = []

# Iterar sobre los conjuros para obtener los detalles
for spell in spells:
    spell_url = f"https://www.dnd5eapi.co{spell['url']}"
    spell_response = requests.get(spell_url)
    if spell_response.status_code != 200:
        print(f"Error al obtener detalles de {spell['name']}: {spell_response.status_code}")
        continue

    spell_details = spell_response.json()
    
    # Extraer datos relevantes
    name = spell_details.get("name", "")
    level = spell_details.get("level", "")
    school = spell_details.get("school", {}).get("name", "")
    description = " ".join(spell_details.get("desc", []))
    damage = spell_details.get("damage", {}).get("damage_at_slot_level", {})

    # Convertir el daño en un formato más manejable
    damage_by_level = "; ".join([f"Nivel {lvl}: {dmg}" for lvl, dmg in damage.items()])

    # Agregar a la lista
    spell_data.append([name, level, school, description, damage_by_level])

# Guardar los datos en un archivo CSV
csv_file = "conjuros_dnd_detallados.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Nivel", "Escuela", "Descripción", "Daño por Nivel"])
    writer.writerows(spell_data)

print(f"Se han guardado {len(spell_data)} conjuros en el archivo {csv_file}.")
