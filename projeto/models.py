from pydantic import BaseModel
from typing import List, Optional

class Professor(BaseModel):
    id: int
    descricao: str
    nome: str
    email: str

class Aluno(BaseModel):
    id: int
    nome: str
    email: str
    curso_id: int
    email: Optional[str] = None  

class Curso(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    professor_id: Optional[int] = None 