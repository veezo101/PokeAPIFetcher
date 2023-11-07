import multiprocessing
import requests
import time

#work-up: move# = 526 and tm# = 18
#get a list of pokemon that learn 526 via "machine" and in version "ultra-sun-ultra-moon"
move_number = 526

base_url = "https://pokeapi.co/api/v2/"

response = requests.get(f"{base_url}move/{move_number}/")
move_data = response.json()

lst_pokemonThatLearn = move_data['learned_by_pokemon']

pokemon_list_names = []
pokemon_list_numbers = []

def task(selectedPokemon):
    selectedPokemonResponse = requests.get(selectedPokemon['url']).json()

    res = []

    lstMoves = selectedPokemonResponse['moves']
    for moveObj in lstMoves:
        if moveObj['move']['name'] == move_data['name']:
            for versionInfo in moveObj['version_group_details']:
                if versionInfo['version_group']['name']=='ultra-sun-ultra-moon':
                    if versionInfo['move_learn_method']['name']=='machine':
                        res.append(selectedPokemon['name'])
                        extracted_dex_num = selectedPokemonResponse['species']['url'].split('/')[-2]
                        if not selectedPokemonResponse["is_default"]:
                            extracted_dex_num += "-form"
                        res.append(extracted_dex_num)
                        
                        break
            break

    return res

if __name__ == '__main__':
    start_time = time.time()
    # add threads based on # of logical processors of your CPU (12 for me) 
    with multiprocessing.Pool(12) as pool:
        for result in pool.map(task, lst_pokemonThatLearn):
            if len(result):
                pokemon_list_names.append(result[0])
                pokemon_list_numbers.append(result[1])
    print("name,number")
    for i in range(len(pokemon_list_numbers)):
        print(pokemon_list_names[i] + "," + pokemon_list_numbers[i])
    
    # uncomment for exec time info
    # print("Elapsed --- %s seconds ---" % (time.time() - start_time))