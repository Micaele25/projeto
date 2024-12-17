from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AlunoModel(Base):
    __tablename__ = 'Aluno'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    curso_id = Column(Integer, ForeignKey('Curso.id'))

    curso = relationship("CursoModel", back_populates="alunos")


class CursoModel(Base):
    __tablename__ = 'Curso'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)

    alunos = relationship("AlunoModel", back_populates="curso")
    professores = relationship("ProfessorModel", back_populates="curso")


class ProfessorModel(Base):
    __tablename__ = 'Professor'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    curso_id = Column(Integer, ForeignKey('Curso.id'))

    curso = relationship("CursoModel", back_populates="professores")
