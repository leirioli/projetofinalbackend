from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float

# conexão com o banco
engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# criação de base do banco de dados
Base = declarative_base()

# criação das tabelas e classes
class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, unique=True, nullable=False)

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    carga_horaria = Column(Integer, nullable=False)

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_aluno = Column(ForeignKey("alunos.id"))
    id_curso = Column(ForeignKey("cursos.id"))
    status = Column(String, default="ativa")