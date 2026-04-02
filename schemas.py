from pydantic import BaseModel

class AlunoSchema(BaseModel):
    nome: str
    email: str
    telefone: str

class AlunoCreate(AlunoSchema):
    pass

class AlunoResponse(AlunoSchema):
    id: int

    class Config:
        from_attributes = True

class CursoSchema(BaseModel):
    nome: str
    descricao: str
    carga_horaria: int

class CursoCreate(CursoSchema):
    pass

class CursoResponse(CursoSchema):
    id: int

    class Config:
        from_attributes: True

class MatriculaSchema(BaseModel):
    id_aluno: int
    id_curso: int

class MatriculaCreate(MatriculaSchema):
    pass

class MatriculaResponse(MatriculaSchema):
    id: int
    status: str

    class Config:
        from_attributes = True