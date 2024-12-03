from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from models import Curso,Aluno, Professor 


cursos = []
alunos = []
professores = []

app = FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.post("/alunos/", response_model=Aluno)
def create_aluno(aluno: Aluno):
    alunos.append(aluno)
    return aluno

@app.get("/alunos/", response_model=List[Aluno])
def get_alunos():
    return alunos

@app.get("/alunos/{aluno_id}", response_model=Aluno)
def get_aluno(aluno_id: int):
    for aluno in alunos:
        if aluno.id == aluno_id:
            return aluno
    return {"error": "Aluno não encontrado"}

@app.put("/alunos/{aluno_id}", response_model=Aluno)
def update_aluno(aluno_id: int, aluno: Aluno):
    for idx, existing_aluno in enumerate(alunos):
        if existing_aluno.id == aluno_id:
            alunos[idx] = aluno
            return aluno
    return {"error": "Aluno não encontrado"}

@app.delete("/alunos/{aluno_id}", response_model=dict)
def delete_aluno(aluno_id: int):
    for idx, aluno in enumerate(alunos):
        if aluno.id == aluno_id:
            del alunos[idx]
            return {"message": "Aluno deletado"}
    return {"error": "Aluno não encontrado"}


@app.post("/cursos/", response_model=Curso)
def create_curso(curso: Curso):
    cursos.append(curso)
    return curso

@app.get("/cursos/", response_model=List[Curso])
def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}", response_model=Curso)
def get_curso(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            return curso
    return {"error": "Curso não encontrado"}

@app.put("/cursos/{curso_id}", response_model=Curso)
def update_curso(curso_id: int, curso: Curso):
    for idx, existing_curso in enumerate(cursos):
        if existing_curso.id == curso_id:
            cursos[idx] = curso
            return curso
    return {"error": "Curso não encontrado"}

@app.delete("/cursos/{curso_id}", response_model=dict)
def delete_curso(curso_id: int):
    for idx, curso in enumerate(cursos):
        if curso.id == curso_id:
            del cursos[idx]
            return {"message": "Curso deletado"}
    return {"error": "Curso não encontrado"}


@app.post("/professores/", response_model=Professor)
def create_professor(professor: Professor):
    professores.append(professor)
    return professor

@app.get("/professores/", response_model=List[Professor])
def get_professores():
    return professores

@app.get("/professores/{professor_id}", response_model=Professor)
def get_professor(professor_id: int):
    for professor in professores:
        if professor.id == professor_id:
            return professor
    return {"error": "Professor não encontrado"}

@app.put("/professores/{professor_id}", response_model=Professor)
def update_professor(professor_id: int, professor: Professor):
    for idx, existing_professor in enumerate(professores):
        if existing_professor.id == professor_id:
            professores[idx] = professor
            return professor
    return {"error": "Professor não encontrado"}

@app.delete("/professores/{professor_id}", response_model=dict)
def delete_professor(professor_id: int):
    for idx, professor in enumerate(professores):
        if professor.id == professor_id:
            del professores[idx]
            return {"message": "Professor deletado"}
    return {"error": "Professor não encontrado"}
