from sqlalchemy import create_engine, Column, Integer, String, BIGINT
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.models.livro import LivroModel
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Livro(Base):
    __tablename__ = "livros"
    id = Column(BIGINT, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)

def criar_tabelas():
    Base.metadata.create_all(bind=engine)

def popular_banco():
    livros = [
        {"id": 9780451524935, "nome": "1984 – George Orwell"},
        {"id": 9780060934347, "nome": "Dom Quixote – Miguel de Cervantes"},
        {"id": 9780141439518, "nome": "Orgulho e Preconceito – Jane Austen"},
        {"id": 9780486415871, "nome": "Crime e Castigo – Fiódor Dostoiévski"},
        {"id": 9780060883287, "nome": "Cem Anos de Solidão – Gabriel García Márquez"},
        {"id": 9780156012195, "nome": "O Pequeno Príncipe – Antoine de Saint-Exupéry"},
        {"id": 9780451526342, "nome": "A Revolução dos Bichos – George Orwell"},
        {"id": 9780743477123, "nome": "Hamlet – William Shakespeare"},
        {"id": 9780199535675, "nome": "Ulisses – James Joyce"},
        {"id": 9780544003415, "nome": "O Senhor dos Anéis – J.R.R. Tolkien"},
        {"id": 9781503280786, "nome": "Moby Dick – Herman Melville"},
        {"id": 9780805210572, "nome": "A Metamorfose – Franz Kafka"},
        {"id": 9780446310789, "nome": "O Sol é para Todos – Harper Lee"},
        {"id": 9780679723165, "nome": "Lolita – Vladimir Nabokov"},
        {"id": 9788520923251, "nome": "Grande Sertão: Veredas – Guimarães Rosa"},
        {"id": 9780316769488, "nome": "O Apanhador no Campo de Centeio – J.D. Salinger"},
        {"id": 9788535911529, "nome": "Ensaio sobre a Cegueira – José Saramago"},
        {"id": 9780743273565, "nome": "O Grande Gatsby – F. Scott Fitzgerald"},
        {"id": 9781451673319, "nome": "Fahrenheit 451 – Ray Bradbury"},
        {"id": 9780140448955, "nome": "A Divina Comédia – Dante Alighieri"},
        {"id": 9786559801367, "nome": "O Pequeno Príncipe – Antoine de Saint-Exupéry"},
        {"id": 9786584956230, "nome": "A Arte da Guerra – Sun Tzu"},
        {"id": 9786585310123, "nome": "Pinóquio – Carlo Collodi"},
        {"id": 9788532530603, "nome": "Percy Jackson e o Ladrão de Raios – Rick Riordan"},
        {"id": 9788578273269, "nome": "As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa – C.S. Lewis"},
        {"id": 9788598078060, "nome": "Artemis Fowl: O Menino Gênio do Crime – Eoin Colfer"},
        {"id": 9788546501458, "nome": "O poder do subconsciente – Joseph Murphy"},
        {"id": 9788576832997, "nome": "Maze Runner: Prova de Fogo – James Dashner"},
        {"id": 9788595084742, "nome": "O Hobbit – J.R.R. Tolkien"},
        {"id": 9786556090696, "nome": "Branca de Neve e os Sete Anões – Irmãos Grimm"},
        {"id": 9788573267389, "nome": "Moby Dick, ou A Baleia – Herman Melville"},
        {"id": 9786555604900, "nome": "Manual de Assassinato para Boas Garotas: 1 – Holly Jackson"},
        {"id": 9788542804126, "nome": "Guerra Civil – Marvel: Uma História do Universo Marvel – Marvel Comics"},
        {"id": 9788543101484, "nome": "Guga, Um Brasileiro – Gustavo Kuerten"},
        {"id": 9788542807578, "nome": "Homem-Aranha Entre Trovões – Marvel Comics"},
        {"id": 9788532290540, "nome": "A Cidade Perdida – Clive Cussler"},
        {"id": 9788572839044, "nome": "O Príncipe de Maquiavel: Texto Integral – Nicolau Maquiavel"},
        {"id": 9788530601492, "nome": "O Guia Definitivo do Mochileiro das Galáxias – Douglas Adams"},
        {"id": 9786558300151, "nome": "Fahrenheit 451 – Edição Especial – Ray Bradbury"},
        {"id": 9788573265996, "nome": "Um Pequeno Herói – Fiódor Dostoiévski"}
    ]
    db = SessionLocal()
    try:
        for livro in livros:
            novo_livro = Livro(**livro)
            db.add(novo_livro)
        db.commit()
        print("livros inseridos com sucesso!")
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.close()

def listar_livros() -> list[LivroModel]:
    db = SessionLocal()
    try:
        livros_db = db.query(Livro).all()
        return [converter_para_pydantic(livro) for livro in livros_db]
    finally:
        db.close()

def converter_para_pydantic(livro_db: Livro) -> LivroModel:
    return LivroModel(
        id=livro_db.id,
        nome=livro_db.nome
    )
if __name__ == "__main__":
    #criar_tabelas()
    #print("Tabelas criadas com sucesso!")
    #popular_banco()
    livros = listar_livros()
    for livro in livros:
        print(f"ID: {livro.id} - Nome: {livro.nome}")