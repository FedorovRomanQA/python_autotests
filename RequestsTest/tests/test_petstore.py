import requests
import pytest

URL = "https://api.pokemonbattle.me/v2"
TOKEN = "9f48fa6c5b0f3f7defda80e29324873f"
HEADER = {"Content-Type": "application/json"}
TRAINER_ID = "2210"


def test_status_code():
    response = requests.get(url=f"{URL}/pokemons", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200
