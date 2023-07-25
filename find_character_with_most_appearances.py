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

def find_character_with_most_appearances():
    api_key = user_api_key
    url = 'https://the-one-api.dev/v2/character'
    headers = {'Authorization': f'Bearer {api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()

        if response.status_code == 200 and response_json['docs']:
            characters = response_json['docs']
            max_appearances = 0
            character_with_most_appearances = None

            for character in characters:
                character_name = character['name']
                character_url = f'https://the-one-api.dev/v2/character/{character["_id"]}/quote'
                quotes_response = requests.get(character_url, headers=headers)
                quotes_json = quotes_response.json()
                appearances = len(quotes_json['docs'])


                if appearances > max_appearances:
                    max_appearances = appearances
                    character_with_most_appearances = character_name
                
                    print(f"The character with the most appearances in movies is '{character_with_most_appearances}'.")
                    print(f"He/she appears in {max_appearances} movies.")
                 
        else:
            print("Failed to retrieve character information.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Find the character with the most appearances in movies
find_character_with_most_appearances()