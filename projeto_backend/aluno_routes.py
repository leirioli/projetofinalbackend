from fastapi import APIRouter

aluno_router = APIRouter(prefix="/alunos", tags=["alunos"])

@aluno_router.get("/")
async def alunos():
    """
    Essa é a rota padrão de alunos no sistema.
    """
    return {"mensagem": "Você acessou a rota de alunos"}