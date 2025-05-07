from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.clients.genai_client import GenAIClient
from app.config.config import Config
from app.models.livro import LivroModel
from app.services.recomendacao_livros import RecomendacaoLivrosService

router = APIRouter()

def get_genai_client():
    return GenAIClient(api_key=Config.api_key)

def get_recomendacao_livros_service(genai_client: GenAIClient = Depends(get_genai_client)):
    return RecomendacaoLivrosService(genai_client)
@router.get("/livros", response_model=List[LivroModel])
def retorna_recomendacoes(
    mensagem: str,
    service: RecomendacaoLivrosService = Depends(get_recomendacao_livros_service),
):
    try:
        return service.get_recomendacoes_livros(mensagem)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))