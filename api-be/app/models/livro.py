from pydantic import BaseModel

class LivroModel(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True