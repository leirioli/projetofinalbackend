from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal
import models
import schemas

curso_router = APIRouter(prefix="/cursos", tags=["cursos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@curso_router.post("/", response_model=schemas.CursoResponse, status_code=201)
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    novo_curso = models.Curso(
        nome=curso.nome, 
        descricao=curso.descricao, 
        carga_horaria=curso.carga_horaria
    )
    
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    
    return novo_curso

@curso_router.get("/", response_model=list[schemas.CursoResponse])
def listar_cursos(db: Session = Depends(get_db)):
    cursos = db.query(models.Curso).all()
    return cursos

@curso_router.get("/{curso_id}", response_model=schemas.CursoResponse)
def procurar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado.")
    return curso

@curso_router.put("/{curso_id}", response_model=schemas.CursoResponse)
def atualizar_curso(curso_id: int, curso_atualizado: schemas.CursoCreate, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado.")

    curso.nome = curso_atualizado.nome
    curso.descricao = curso_atualizado.descricao
    curso.carga_horaria = curso_atualizado.carga_horaria

    db.commit()
    db.refresh(curso)
    return curso

@curso_router.delete("/{curso_id}", status_code=204)
def eliminar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado.")

    db.delete(curso)
    db.commit()
    return