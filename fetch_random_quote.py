import random
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

def fetch_random_quote():
    api_key = user_api_key
    url = 'https://the-one-api.dev/v2/quote'
    headers = {'Authorization': f'Bearer {api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()

        if response.status_code == 200 and response_json['docs']:
            quote = random.choice(response_json['docs'])
            print("Quote:", quote['dialog'])
            print("Movie:", quote['movie'])
            print("Character:", quote['character'])
        else:
            print("Failed to fetch a random quote.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Fetch and display a random quote
fetch_random_quote()