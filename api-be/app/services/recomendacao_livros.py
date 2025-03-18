from app.clients.genai_client import GenAIClient

class RecomendacaoLivrosService:
    def __init__(self, genai_client: GenAIClient):
        self.genai_client = genai_client

    def  get_recomendacoes_livros(self, mensagem: str):
        return self.genai_client.gerar_resposta(mensagem)

