
superheroes = [35, 69, 104, 149]

import requests
import pprint

def get_the_smartest_superhero(superheros):
    the_smartest_superhero = ''
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        filtered_heroes = [hero for hero in data if hero['id'] in superheroes]

        result_dict = {
            hero['name']: hero['powerstats']['intelligence']
            for hero in filtered_heroes
        }

        the_smartest_superhero = max(result_dict, key=result_dict.get)
        return the_smartest_superhero
    except Exception as e:
        print(f'Something went wrong: {e}')

print(get_the_smartest_superhero(superheroes))