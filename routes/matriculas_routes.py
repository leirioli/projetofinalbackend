from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal
import models
import schemas

matriculas_router = APIRouter(prefix="/matriculas", tags=["matriculas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@matriculas_router.post("/", response_model=schemas.MatriculaResponse, status_code=201)
def matricular_aluno(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == matricula.id_aluno).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    curso = db.query(models.Curso).filter(models.Curso.id == matricula.id_curso).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado.")

    matricula_existente = db.query(models.Matricula).filter(
        models.Matricula.id_aluno == matricula.id_aluno,
        models.Matricula.id_curso == matricula.id_curso
    ).first()
    
    if matricula_existente:
        raise HTTPException(status_code=400, detail="O aluno já está matriculado neste curso.")

    total_matriculas_ativas = db.query(models.Matricula).filter(
        models.Matricula.id_aluno == matricula.id_aluno,
        models.Matricula.status == "ativa"
    ).count()
    
    if total_matriculas_ativas >= 5:
        raise HTTPException(status_code=400, detail="O aluno atingiu o limite máximo de 5 matrículas ativas.")

    nova_matricula = models.Matricula(
        id_aluno=matricula.id_aluno,
        id_curso=matricula.id_curso,
        status="ativa"
    )
    
    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)
    
    return nova_matricula

@matriculas_router.get("/aluno/{aluno_id}", response_model=list[schemas.MatriculaResponse])
def listar_cursos_do_aluno(aluno_id: int, db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).filter(models.Matricula.id_aluno == aluno_id).all()
    return matriculas

@matriculas_router.get("/curso/{curso_id}", response_model=list[schemas.MatriculaResponse])
def listar_alunos_do_curso(curso_id: int, db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).filter(models.Matricula.id_curso == curso_id).all()
    return matriculas

@matriculas_router.patch("/{matricula_id}/cancelar", response_model=schemas.MatriculaResponse)
def cancelar_matricula(matricula_id: int, db: Session = Depends(get_db)):
    matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada.")

    matricula.status = "cancelada"
    db.commit()
    db.refresh(matricula)
    return matricula

@matriculas_router.patch("/{matricula_id}/concluir", response_model=schemas.MatriculaResponse)
def concluir_matricula(matricula_id: int, db: Session = Depends(get_db)):
    matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada.")

    matricula.status = "concluida"
    db.commit()
    db.refresh(matricula)
    return matricula