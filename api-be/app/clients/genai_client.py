from google import genai

class GenAIClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def gerar_resposta(self, mensagem: str):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=mensagem
        )
        if response:
            return response.text
        else:
            raise Exception('Erro ao enviar mensagem para gemini ai')