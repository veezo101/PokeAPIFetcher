import requests

#work-up: move# = 526 and tm# = 18
move_number = 526

base_url = "https://pokeapi.co/api/v2/"

response = requests.get(f"{base_url}move/{move_number}/")
move_data = response.json()

# Extract the moves that the TM teaches
lst_pokemonThatLearn = move_data['learned_by_pokemon']

# Iterate through the moves and get the Pokémon that can learn each move
pokemon_list = []
for selectedPokemon in lst_pokemonThatLearn:
    selectedPokemonResponse = requests.get(selectedPokemon['url'])
    lstMoves = selectedPokemonResponse.json()['moves']
    for moveObj in lstMoves:
        for versionInfo in moveObj['version_group_details']:
            if versionInfo['version_group']['name']=='ultra-sun-ultra-moon':
                if versionInfo['move_learn_method']['name']=='machine':
                    print(f"{selectedPokemon['name']} - {moveObj['move']['name']}")