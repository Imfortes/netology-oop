import requests
import pprint



def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    target_heroes = {'Hulk', 'Captain America', 'Thanos'}
    # url = 'https://akabab.github.io/superhero-api/api/all.json'
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        pprint.pp(data)

        result_dict = {
            hero['name']: hero['powerstats']['intelligence']
            for hero in data
            if hero['name'] in target_heroes
        }

        the_smartest_superhero = max(result_dict, key=result_dict.get)

        return the_smartest_superhero
    except Exception as e:
        print(f'Something went wrong: {e}')

print(get_the_smartest_superhero())

