from pydantic import BaseModel

class Livro(BaseModel):
    id: int
    nome: str
