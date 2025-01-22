from pydantic import BaseModel

class Aluno(BaseModel):
    id: int
    nome: str
    idade: int
    curso_id: int

class Curso(BaseModel):
    id: int
    nome: str
    descricao: str

class Professor(BaseModel):
    id: int
    nome: str
    especialidade: str
