import requests

URL = "https://api.pokemonbattle.me/v2"
TOKEN = "9f48fa6c5b0f3f7defda80e29324873f"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
body_create = {"name": "generate", "photo": "generate"}
body_change = {"pokemon_id": "26682", "name": "generate"}
body_katch = {"pokemon_id": "26595"}

# Создать покемона
response_create = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=body_create)
print(response_create.text)

# Изменить покемона
response_change = requests.patch(
    url=f"{URL}/pokemons", headers=HEADER, json=body_change
)
print(response_change.text)

# Поймать покемона
response_katch = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_katch
)
print(response_katch.text)
