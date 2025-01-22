from fastapi import FastAPI, Form, Request
from app.routers import router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import HTMLResponse

app = FastAPI()

# Incluindo o roteador principal
app.include_router(router)

# Configurando o diretório dos templates Jinja2
templates = Jinja2Templates(directory="app/templates")

# Configurando o diretório estático (CSS, imagens, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Simulando um banco de dados com listas (para fins de teste)
alunos = []
cursos = []
professores = []

# Rota para renderizar o template da página inicial
@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "alunos": alunos,
        "cursos": cursos,
        "professores": professores
    })

# Rota adicional para uma resposta JSON
@app.get("/api")
def root():
    return {"message": "API de Gerenciamento de Alunos, Cursos e Professores"}
@app.get("/editar/{tipo}/{id}")
def editar(tipo: str, id: int):
    # Lógica para editar o registro
    pass
@app.get("/adicionar/aluno")
def adicionar_aluno():
    # Lógica para exibir o formulário de adicionar aluno
    pass
@app.get("/adicionar/aluno", response_class=HTMLResponse)
async def adicionar_aluno(request: Request):
    return templates.TemplateResponse("form_aluno.html", {"request": request})

@app.get("/listar/alunos")
def listar_alunos():
    # Lógica para listar alunos
    pass

@app.get("/deletar/aluno")
def deletar_aluno():
    # Lógica para deletar aluno
    pass

@app.get("/adicionar/curso")
def adicionar_curso():
    # Lógica para exibir o formulário de adicionar curso
    pass

@app.get("/listar/cursos")
def listar_cursos():
    # Lógica para listar cursos
    pass

@app.get("/deletar/curso")
def deletar_curso():
    # Lógica para deletar curso
    pass

@app.get("/adicionar/professor")
def adicionar_professor():
    # Lógica para exibir o formulário de adicionar professor
    pass

@app.get("/listar/professores")
def listar_professores():
    # Lógica para listar professores
    pass

@app.get("/deletar/professor")
def deletar_professor():
    # Lógica para deletar professor
    pass
