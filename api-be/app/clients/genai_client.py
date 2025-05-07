from google import genai
from rapidfuzz import fuzz
from app.models.livro import LivroModel
from app.utils import mensagens
from app.models.database import listar_livros

class GenAIClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def gerar_resposta(self, mensagem: str):
        mensagem = mensagens.formatar_mensagem(mensagem)
        condicao = "\nMe retorne esses dados no formato JSON"
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=mensagem + condicao,
            config={
                'response_mime_type': 'application/json',
                'response_schema': list[LivroModel],
            },
        )
        if(response):
            livros_recomendados: list[LivroModel] = response.parsed
            livros_salvos = listar_livros()
            livros_filtrados = self.filtrar_livros_existentes(livros_recomendados, livros_salvos)
            return livros_filtrados
        else:
            raise Exception('Erro ao enviar mensagem para gemini ai')

    @staticmethod
    def filtrar_livros_existentes(livros_recomendados, livros_salvos):
        SIMILARIDADE_MINIMA = 70
        livros_por_id = {livro.id: livro for livro in livros_salvos}
        livros_por_nome = {livro.nome.lower(): livro for livro in livros_salvos}
        nomes_salvos = list(livros_por_nome.keys())
        resultado = []
        for livro in livros_recomendados:
            if livro.id in livros_por_id:
                resultado.append(livros_por_id[livro.id])
                continue
            nome_livro = livro.nome.lower()
            melhor_match, melhor_score = max(
                ((nome_salvo, fuzz.ratio(nome_livro, nome_salvo)) for nome_salvo in nomes_salvos),
                key=lambda x: x[1]
            )
            if melhor_score >= SIMILARIDADE_MINIMA:
                resultado.append(livros_por_nome[melhor_match])
        return resultado
