import requests

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
def fetch_character_info(character_name):
    api_key = user_api_key
    url = f'https://the-one-api.dev/v2/character?name={character_name}'
    headers = {'Authorization': f'Bearer {api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()

        if response.status_code == 200 and response_json['docs']:
            character = response_json['docs'][0]
            print(f"Name: {character['name']}")
            print(f"Race: {character['race']}")
            print(f"Gender: {character['gender']}")
            print(f"Birth: {character['birth']}")
            print(f"Death: {character['death']}")
        else:
            print(f"Character '{character_name}' not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Prompt the user for a character name
character_name = input("Enter the name of a character from 'The Lord of the Rings' universe: ")
fetch_character_info(character_name)