from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True
