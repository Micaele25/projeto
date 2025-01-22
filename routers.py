from fastapi import APIRouter, HTTPException
from app.models import Aluno, Curso, Professor
from typing import List

router = APIRouter()

# ==== Dados em memória ====
alunos: List[Aluno] = []
cursos: List[Curso] = []
professores: List[Professor] = []

# ==== Rotas para alunos ====
@router.get("/alunos/", response_model=List[Aluno])
def listar_alunos():
    return alunos

@router.post("/alunos/", response_model=Aluno)
def criar_aluno(aluno: Aluno):
    if any(a.id == aluno.id for a in alunos):
        raise HTTPException(status_code=400, detail="Aluno com este ID já existe.")
    alunos.append(aluno)
    return aluno

@router.put("/alunos/{aluno_id}", response_model=Aluno)
def atualizar_aluno(aluno_id: int, aluno_atualizado: Aluno):
    for index, aluno in enumerate(alunos):
        if aluno.id == aluno_id:
            alunos[index] = aluno_atualizado
            return aluno_atualizado
    raise HTTPException(status_code=404, detail="Aluno não encontrado.")

@router.delete("/alunos/{aluno_id}")
def deletar_aluno(aluno_id: int):
    for index, aluno in enumerate(alunos):
        if aluno.id == aluno_id:
            alunos.pop(index)
            return {"detail": "Aluno deletado com sucesso."}
    raise HTTPException(status_code=404, detail="Aluno não encontrado.")

# ==== Rotas para cursos ====
@router.get("/cursos/", response_model=List[Curso])
def listar_cursos():
    return cursos

@router.post("/cursos/", response_model=Curso)
def criar_curso(curso: Curso):
    if any(c.id == curso.id for c in cursos):
        raise HTTPException(status_code=400, detail="Curso com este ID já existe.")
    cursos.append(curso)
    return curso

@router.put("/cursos/{curso_id}", response_model=Curso)
def atualizar_curso(curso_id: int, curso_atualizado: Curso):
    for index, curso in enumerate(cursos):
        if curso.id == curso_id:
            cursos[index] = curso_atualizado
            return curso_atualizado
    raise HTTPException(status_code=404, detail="Curso não encontrado.")

@router.delete("/cursos/{curso_id}")
def deletar_curso(curso_id: int):
    for index, curso in enumerate(cursos):
        if curso.id == curso_id:
            cursos.pop(index)
            return {"detail": "Curso deletado com sucesso."}
    raise HTTPException(status_code=404, detail="Curso não encontrado.")

# ==== Rotas para professores ====
@router.get("/professores/", response_model=List[Professor])
def listar_professores():
    return professores

@router.post("/professores/", response_model=Professor)
def criar_professor(professor: Professor):
    if any(p.id == professor.id for p in professores):
        raise HTTPException(status_code=400, detail="Professor com este ID já existe.")
    professores.append(professor)
    return professor

@router.put("/professores/{professor_id}", response_model=Professor)
def atualizar_professor(professor_id: int, professor_atualizado: Professor):
    for index, professor in enumerate(professores):
        if professor.id == professor_id:
            professores[index] = professor_atualizado
            return professor_atualizado
    raise HTTPException(status_code=404, detail="Professor não encontrado.")

@router.delete("/professores/{professor_id}")
def deletar_professor(professor_id: int):
    for index, professor in enumerate(professores):
        if professor.id == professor_id:
            professores.pop(index)
            return {"detail": "Professor deletado com sucesso."}
    raise HTTPException(status_code=404, detail="Professor não encontrado.")
