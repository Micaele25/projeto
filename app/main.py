from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from typing import List
from .database import get_db
from .schema import AlunoBase as AlunoSchema


app = FastAPI()

@app.post("/alunos/", response_model=AlunoSchema)
def create_aluno(aluno: AlunoSchema, db: Session = Depends(get_db)):
    db_aluno = models.AlunoModel(**aluno.dict())  # Usando AlunoModel aqui
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    result = db.query(models.AlunoModel).all()  # Corrigido para AlunoModel
    return {"result": result}

@app.get("/alunos/", response_model=List[AlunoSchema])
def get_alunos(db: Session = Depends(get_db)):
    return db.query(models.AlunoModel).all()

@app.get("/alunos/{aluno_id}", response_model=AlunoSchema)
def get_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.AlunoModel).filter(models.AlunoModel.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@app.put("/alunos/{aluno_id}", response_model=AlunoSchema)
def update_aluno(aluno_id: int, aluno: AlunoSchema, db: Session = Depends(get_db)):
    db_aluno = db.query(models.AlunoModel).filter(models.AlunoModel.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    for key, value in aluno.dict().items():
        setattr(db_aluno, key, value)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

@app.delete("/alunos/{aluno_id}", response_model=dict)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(models.AlunoModel).filter(models.AlunoModel.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(db_aluno)
    db.commit()
    return {"message": "Aluno deletado"}
