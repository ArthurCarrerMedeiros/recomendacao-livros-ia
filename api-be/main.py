from fastapi import FastAPI
from api.routers.recomendacao_livros import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)