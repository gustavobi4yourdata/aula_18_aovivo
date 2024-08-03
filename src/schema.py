from pydantic import BaseModel

# View de como os dados vão vir (API)
class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True