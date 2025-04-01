from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.recomendacao_livros import router

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)