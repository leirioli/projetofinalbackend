from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from models import SessionLocal
import schemas

aluno_router = APIRouter(prefix="/alunos", tags=["alunos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@aluno_router.post("/", response_model=schemas.AlunoResponse, status_code=201)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    email_existe = db.query(models.Aluno).filter(models.Aluno.email == aluno.email).first()
    if email_existe:
        raise HTTPException(status_code=400, detail="Este e-mail já está registrado.")
        
    telefone_existe = db.query(models.Aluno).filter(models.Aluno.telefone == aluno.telefone).first()
    if telefone_existe:
        raise HTTPException(status_code=400, detail="Este telefone já está registrado.")

    novo_aluno = models.Aluno(
        nome=aluno.nome, 
        email=aluno.email, 
        telefone=aluno.telefone
    )
    
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

@aluno_router.get("/", response_model=list[schemas.AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    alunos = db.query(models.Aluno).all()
    return alunos

@aluno_router.get("/{aluno_id}", response_model=schemas.AlunoResponse)
def procurar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
        
    return aluno

@aluno_router.put("/{aluno_id}", response_model=schemas.AlunoResponse)
def atualizar_aluno(aluno_id: int, aluno_atualizado: schemas.AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    aluno.nome = aluno_atualizado.nome
    aluno.email = aluno_atualizado.email
    aluno.telefone = aluno_atualizado.telefone

    db.commit()
    db.refresh(aluno)
    return aluno

@aluno_router.delete("/{aluno_id}", status_code=204)
def eliminar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    db.delete(aluno)
    db.commit()
    return