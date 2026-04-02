from fastapi import APIRouter

curso_router = APIRouter(prefix="/cursos", tags=["cursos"])

@curso_router.get("/")
async def cursos():
    """
    Essa á a rota padrão de cursos no nosso sistema. O aluno precisa estar cadastrado para ter acesso aos cursos.
    """
    return {"mensagem": "Você acessou a rota de cursos"}
