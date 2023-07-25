import requests 


# get api key from text
def get_api_key():
    try:
        with open('api_key.txt', 'r') as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print("Error: 'api_key.txt' not found.")
        return None
 # api key    
user_api_key = get_api_key()

def search_characters_by_race(race):
    api_key = user_api_key
    url = f'https://the-one-api.dev/v2/character?race={race}'
    headers = {'Authorization': f'Bearer {api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()

        if response.status_code == 200 and response_json['docs']:
            print(f"Characters belonging to the race '{race}':")
            for character in response_json['docs']:
                print(character['name'])
        else:
            print(f"No characters found belonging to the race '{race}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Prompt the user for a race to search for characters
race = input("Enter the race to search for characters: ")
search_characters_by_race(race)