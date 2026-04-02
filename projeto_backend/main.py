from fastapi import FastAPI
import models
from models import engine

# criação do banco de dados
models.Base.metadata.create_all(bind=engine)

# chamando a instância FastAPI para a criação do app
app = FastAPI()

# importação das rotas
from aluno_routes import aluno_router
from curso_routes import curso_router

app.include_router(aluno_router)
app.include_router(curso_router)

# executar -> uvicorn main:app --reload

