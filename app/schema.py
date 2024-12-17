from pydantic import BaseModel
from typing import Optional, List

class AlunoBase(BaseModel):
    nome: str
    email: Optional[str]
    curso_id: int

class AlunoCreate(AlunoBase):
    pass

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True


class CursoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CursoCreate(CursoBase):
    pass

class CursoResponse(CursoBase):
    id: int
    alunos: List[AlunoResponse] = []
    professores: List["ProfessorResponse"] = []

    class Config:
        from_attributes = True


class ProfessorBase(BaseModel):
    nome: str
    email: Optional[str] = None

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorResponse(ProfessorBase):
    id: int
    curso_id: Optional[int]

    class Config:
        from_attributes = True
