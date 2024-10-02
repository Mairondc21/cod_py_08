import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int):

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    print(data['name'], types)

    return PokemonSchema(name=data['name'],type=types)


if __name__ == "__main__":
    pegar_pokemon(6)
    pegar_pokemon(21)
    pegar_pokemon(33)