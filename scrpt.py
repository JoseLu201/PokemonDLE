import requests
from bs4 import BeautifulSoup
import numpy as np
from Pokemon import *
# URL of the webpage with the table
def getPokedex():
    url = 'https://pokemondb.net/pokedex/all'
    response = requests.get(url)


    if response.status_code == 200:
        # Parsear el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar la tabla que contiene los datos de los Pokémon
        table = soup.find('table', {'id': 'pokedex'})

        if table:
            # Crear una lista para almacenar los datos de los Pokémon
            pokemon_data = []

            # Iterar a través de las filas de la tabla
            for row in table.find_all('tr')[1:]:  # Ignorar la primera fila de encabezado
                columns = row.find_all('td')

                if len(columns) > 0:
                    # Crear una lista para almacenar los datos de una fila de Pokémon
                    row_data = []
                    
                    for cell in columns:
                        small_tag = cell.find('small')
                        a_tags = cell.find_all('a')
                        
                        if small_tag:
                            # Si se encuentra una etiqueta <small>, obtener su contenido
                            row_data.append(small_tag.get_text(strip=True).lower())
                        elif a_tags:
                            # Si hay etiquetas <a>, obtener su contenido en una lista
                            a_contents = [a.get_text(strip=True).lower() for a in a_tags]
                            if len(a_contents) == 1:
                                row_data.append(a_contents[0].lower())  # Almacenar como una cadena si solo hay un elemento
                            else:
                                row_data.append(a_contents)
                        else:
                            # En otros casos, obtener el contenido de la celda
                            row_data.append(cell.get_text(strip=True).lower())
                        
                    # Agregar los datos de la fila a la lista de Pokémon
                    pokemon_data.append(row_data)
    arr_pokemon = []
    for poke in pokemon_data:
        # print(poke)
        pok = Pokemon(*poke)
        arr_pokemon.append(pok)
    return arr_pokemon


def getRandomPokemon(pokedex):
    return pokedex[np.random.randint(0,len(pokedex))]

def getColors(coincidencias):

    color = []
    for c in coincidencias:
        if c == '!=':
            color.append(f'background-color: red;')
        elif c == '=':
            color.append(f'background-color: green;')
        else:
            color.append(f'background-color: yellow;')
    return color
