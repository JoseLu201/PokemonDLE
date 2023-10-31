import requests
import bs4
from bs4 import BeautifulSoup
import numpy as np
from Pokemon import *
import ast
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
                        small_tag = cell.find('small') # Aqui esta el subnombre
                        a_tags = cell.find_all('a') # Aqui esta el nombre
                        
                        if small_tag:
                            # Si se encuentra una etiqueta <small>, obtener su contenido
                            row_data.append(small_tag.get_text(strip=True).lower())
                        elif a_tags:
                            # Si hay etiquetas <a>, obtener su contenido en una lista
                            a_contents = [a.get_text(strip=True).lower() for a in a_tags]
                            # if len(a_contents) == 1:
                            #     row_data.append(a_contents[0].lower())  # Almacenar como una cadena si solo hay un elemento
                            # else:
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


def getPokedex_extend():
    url = 'https://pokemondb.net/pokedex/all'
    response = requests.get(url)
    pokedex = []


    if response.status_code == 200:
        # Parsear el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar la tabla que contiene los datos de los Pokémon
        table = soup.find('table', {'id': 'pokedex'})

        if table:
            # Crear una lista para almacenar los datos de los Pokémon
            

            # Iterar a través de las filas de la tabla
            for row in table.find_all('tr')[1:]:  # Ignorar la primera fila de encabezado
                columns = row.find_all('td')

                if len(columns) > 0:
                    pokemon_data = []
                    for cell in columns:
                        imagen = cell.find('img')
                        classes = cell.get('class', [])
    
                        if imagen:
                            imagen_url = imagen.get('src') 
                            # print(imagen_url)
                            pokemon_data.append(imagen_url)
                        
                        if 'cell-name' in classes:
                            pokemon_name = cell.find('a', class_='ent-name')
                            pokemon_subname = cell.find('small', class_='text-muted')
                            pokemon_names = []
                            if pokemon_name:
                                pokemon_names.append(pokemon_name.text)
                            if pokemon_subname:
                                pokemon_names.append(pokemon_subname.text)
                            # print(pokemon_names)
                            pokemon_data.append(pokemon_names)
                                
                        
                        if 'cell-icon' in classes:
                            pokemons_types = []
                            html_types = list(cell.find_all('a', class_='type-icon'))
                            for p in html_types:
                                pokemons_types.append(p.text)
                            if pokemons_types:
                                # print(pokemons_types)
                                pokemon_data.append(pokemons_types)
                        
                        if 'cell-num' in classes:
                            # print(cell.text)
                            if cell.text:
                                pokemon_data.append(cell.text)
                        
                        if 'cell-name' in classes:
                            html_gen = cell.find('a')
                            url_gen = "https://pokemondb.net"+html_gen.get('href')
                            # print(url_gen)
                            response = requests.get(url_gen)
                            # Comprueba si la solicitud se realizó con éxito
                            if response.status_code == 200:
                                # Analiza el contenido HTML de la página
                                soup = BeautifulSoup(response.text, 'html.parser')

                                # Encuentra la sección que contiene la información de la generación
                                generation_section = soup.find('abbr')
                                if generation_section:
                                    # print(generation_section.text)
                                    pokemon_data.append(generation_section.text)
                        
                    pokedex.append(pokemon_data)           
    arr_pokemon = []
    for poke in pokedex:
        print(poke)
        # pok = Pokemon(*poke)
        # arr_pokemon.append(pok)
    # return arr_pokemon

# getPokedex_extend()

def createPokedex(file):
    arr_pokemon = []
    with open(file, 'r') as f:
        for line in f:
            try:
                array = ast.literal_eval(line.strip())
                if isinstance(array, list):
                    if len(array[4]) == 1:
                        array[4].append('None')
                    arr_pokemon.append(Pokemon(*array))
            except (ValueError, SyntaxError):
                # Handle invalid lines that can't be interpreted as lists
                pass
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
