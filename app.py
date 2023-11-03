from flask import Flask, render_template, request
from Pokemon import *
import scrpt
app = Flask(__name__)

# Datos de ejemplo de Pokémon (puedes cargar datos desde una base de datos)
pokemon_data = scrpt.createPokedex('pokedex.txt')
secret_pokemon = scrpt.getRandomPokemon(pokemon_data)
results = []
search_results = []
pokemon_names = []
@app.route('/')
def index():
    for p in pokemon_data:
        p.name[0] = " ".join(p.name)
    pokemon_names = [pokemon.name[0] for pokemon in pokemon_data]
    pokemon_names.sort()
    return render_template('index.html', pokemon_names=pokemon_names)

@app.route('/search', methods=['GET'])
def search_pokemon():
    pokemon_names = [pokemon.name[0] for pokemon in pokemon_data]
    pokemon_names.sort()
    search_query = request.args.get('search_query')
    pokemon_find = None
    if search_query:
        for pokemon in pokemon_data:
            if search_query.lower().__eq__(pokemon.name[0].lower()):
                results.append(pokemon)
                pokemon_names.remove(pokemon.name[0])
                pokemon_find = pokemon

    coincidencias = secret_pokemon.compare(pokemon_find)
    colors = scrpt.getColors(coincidencias)
    # Verifica si se encontró un Pokémon
    if pokemon_find:
        
        div_structure = f'''
        <div class="square-container">
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px);">
                <div class="square-content"> {pokemon_find.name[0]}</div>
                
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[0]}">
                <div class="square-content"> {pokemon_find.types[0]} {coincidencias[0]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[1]}">
                <div class="square-content"> {pokemon_find.types[1]} {coincidencias[1]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[2]}">
                <div class="square-content"> {pokemon_find.total}
                {coincidencias[2]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[3]}">
                <div class="square-content"> {pokemon_find.hp}
                {coincidencias[3]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[4]}">
                <div class="square-content">{pokemon_find.attack}
                {coincidencias[4]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[5]}">
                <div class="square-content">  {pokemon_find.defense}
                {coincidencias[5]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[6]}">
                <div class="square-content">  {pokemon_find.spAtk}
                {coincidencias[6]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[7]}">
                <div class="square-content">  {pokemon_find.spDef}
                {coincidencias[7]}</div>
            </div>
            <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[8]}">
                <div class="square-content">  {pokemon_find.speed}
                {coincidencias[8]}</div>
            </div>
             <div class="square square-title" style="flex-basis: calc(9.09% - 4px); {colors[9]}">
                <div class="square-content">  {pokemon_find.gen}
                {coincidencias[9]}</div>
            </div>
        </div>
        '''
    else:
        div_structure = ''  # Si no se encontró ningún Pokémon, div_structure estará vacío
    search_results.insert(0,div_structure)


    return render_template('index.html', search_results=search_results, pokemon_names=pokemon_names, secret_pokemon=secret_pokemon)



if __name__ == '__main__':
    app.run(debug=True)
