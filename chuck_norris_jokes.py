import requests

def fetch_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    joke_data = response.json()

    if response.status_code == 200:
        joke = joke_data['value']
        print(joke)
    else:
        print("Error occurred while fetching a joke.")

fetch_joke()
