import requests

#work-up: move# = 526 and tm# = 18
move_number = 526

base_url = "https://pokeapi.co/api/v2/"

response = requests.get(f"{base_url}move/{move_number}/")
move_data = response.json()

lst_pokemonThatLearn = move_data['learned_by_pokemon']

pokemon_list_names = []
pokemon_list_numbers = []

for selectedPokemon in lst_pokemonThatLearn:
    selectedPokemonResponse = requests.get(selectedPokemon['url']).json()
    lstMoves = selectedPokemonResponse['moves']
    for moveObj in lstMoves:
        if moveObj['move']['name'] == move_data['name']:
            for versionInfo in moveObj['version_group_details']:
                if versionInfo['version_group']['name']=='ultra-sun-ultra-moon':
                    if versionInfo['move_learn_method']['name']=='machine':
                        pokemon_list_names.append(selectedPokemon['name'])
                        speciesResponse = requests.get(selectedPokemonResponse['species']['url'])
                        species_data = speciesResponse.json()
                        pokemon_list_numbers.append(species_data['id'])
                        print(pokemon_list_names)
                        print(pokemon_list_numbers)
                        break
            break
print(pokemon_list_names)
print(pokemon_list_numbers)