# PokeAPIFetcher
Python scripts to fetch and filter data from [PokeAPI](https://pokeapi.co/docs/v2)

## Setup
[Optional] Make and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Run Script\
In this case, the output is displayed on the Terminal itself
```bash
python tmpuller.py
```
Alternatively, send the output to a csv file.
```bash
python tmpuller.py > output.csv
```
Remember to deactive your v-env when done
```bash
deactive
```
## Configuration
Currently, the `tmpuller.py` script is set to pull "a list of all Pokemon that learn the move `work up` via `TM` for version `ultra-sun & ultra-moon`.\
These filters must be adjusted in the revelant conditions on the code in case of other uses.

The ID of the move work up, as  specified by PokeAPI was obtained by making an API call to the endpoint:
```bash
GET https://pokeapi.co/api/v2/move/?offset=100&limit=500
```
One may adjust the offset and limit as per their paging needs. Using the output list of moves, a simple but manual ctrl+f for `Workup` was ran, to get the respective ID. This ID can then be used in further API calls described in the python scripts.

## Handling Forms
The script describes forms as any Pokemon with the `is_default` bool returned from PokeAPI as `false`. In this case, the `number` in the csv output is appended with a `"-form"` string. These can appended numbers can then be filtered to decide on any manual actions taken on Form Pokemon.



## Output
The expected output from the the script can be found in [test.csv](./test.csv)

## Future Ideas
More scripts for specialized fetching for:
- Generation wise learnset of Pokemon etc