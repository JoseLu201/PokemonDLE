from flask import Flask, render_template, request
from Pokemon import *
import scrpt
app = Flask(__name__)

# Datos de ejemplo de Pokémon (puedes cargar datos desde una base de datos)
pokemon_data = scrpt.getPokedex()
secret_pokemon = scrpt.getRandomPokemon(pokemon_data)
results = []
search_results = []
pokemon_names = []
@app.route('/')
def index():
    pokemon_names = [pokemon.name for pokemon in pokemon_data]
    return render_template('index.html', pokemon_names=pokemon_names)

@app.route('/search', methods=['GET'])
def search_pokemon():
    pokemon_names = [pokemon.name for pokemon in pokemon_data]
    pokemon_names.sort()
    search_query = request.args.get('search_query')
    pokemon_find = None
    if search_query:
        for pokemon in pokemon_data:
            if search_query.lower().__eq__(pokemon.name):
                results.append(pokemon)
                # pokemon_data.remove(pokemon)
                pokemon_find = pokemon

    coincidencias = secret_pokemon.compare(pokemon_find)
    colors = scrpt.getColors(coincidencias)
    # Verifica si se encontró un Pokémon
    if pokemon_find:
        
        div_structure = f'''
        <div class="square-container">
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px);">
                <div class="square-content"> {pokemon_find.name}</div>
                
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[0]}">
                <div class="square-content"> {pokemon_find.types} {coincidencias[0]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[1]}">
                <div class="square-content"> {pokemon_find.total}
                {coincidencias[1]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[2]}">
                <div class="square-content"> {pokemon_find.hp}
                {coincidencias[2]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[3]}">
                <div class="square-content">{pokemon_find.attack}
                {coincidencias[3]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[4]}">
                <div class="square-content">  {pokemon_find.defense}
                {coincidencias[4]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[5]}">
                <div class="square-content">  {pokemon_find.spAtk}
                {coincidencias[5]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[6]}">
                <div class="square-content">  {pokemon_find.spDef}
                {coincidencias[6]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(11.1% - 4px); {colors[7]}">
                <div class="square-content">  {pokemon_find.speed}
                {coincidencias[7]}</div>
            </div>
        </div>
        '''
    else:
        div_structure = ''  # Si no se encontró ningún Pokémon, div_structure estará vacío
    search_results.insert(0,div_structure)


    return render_template('index.html', search_results=search_results, secret_pokemon=secret_pokemon, pokemon_names=pokemon_names)



if __name__ == '__main__':
    app.run(debug=True)
