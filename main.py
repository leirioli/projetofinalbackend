from fastapi import FastAPI, Request
import models
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

# chamando a instância FastAPI para a criação do app
app = FastAPI()

# importação das rotas
from routes.aluno_routes import aluno_router
from routes.curso_routes import curso_router
from routes.matriculas_routes import matriculas_router

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    mensagem = exc.detail

    if exc.status_code == 400:
        mensagem = "Requisição inválida"
    elif exc.status_code == 404:
        mensagem = "Recurso não encontrado"

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": mensagem,
            "statusCode": exc.status_code
        }
    )

app.include_router(aluno_router)
app.include_router(curso_router)
app.include_router(matriculas_router)

# executar -> uvicorn main:app --reload

