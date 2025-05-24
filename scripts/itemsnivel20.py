import requests
from bs4 import BeautifulSoup

# URL de l'item detallat
item_url = 'https://nivel20.com/games/dnd-5/rulebooks/4-reglas-basicas/items/780-dardo'

# Realitzar la petició GET a la pàgina de l'item
response = requests.get(item_url)

if response.status_code == 200:
    item_soup = BeautifulSoup(response.text, 'html.parser')

    # Comprovació abans d'accedir al text
    item_name_tag = item_soup.find('h4', class_='modal-title')
    if item_name_tag:
        item_name = item_name_tag.get_text(strip=True)
    else:
        item_name = "Nom no trobat"

    # Extreure altres dades, afegint comprovacions
    item_type_tag = item_soup.find('strong', text='Tipo de objeto')
    if item_type_tag:
        item_type = item_type_tag.find_next('p').get_text(strip=True)
    else:
        item_type = "Tipus no trobat"
    
    # Imprimir els resultats
    print(f"Nom: {item_name}")
    print(f"Tipus: {item_type}")
else:
    print(f"Error en la petició: {response.status_code}")
