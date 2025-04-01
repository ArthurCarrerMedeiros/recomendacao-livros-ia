from google import genai
from app.models.livro import Livro

class GenAIClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def gerar_resposta(self, mensagem: str):
        condicao = "\nMe retorne esses dados no formato JSON"
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=mensagem + condicao,
            config={
                'response_mime_type': 'application/json',
                'response_schema': list[Livro],
            },
        )
        if(response):
            livros_recomendados: list[Livro] = response.parsed
            print(livros_recomendados)
        else:
            raise Exception('Erro ao enviar mensagem para gemini ai')