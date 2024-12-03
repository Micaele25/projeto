# Projeto API Educação

## Descrição
Este projeto é uma API simples para gerenciar cursos, alunos e professores em uma instituição de ensino. Ele permite criar,puxar,atualizar e excluir alunos, cursos e professores.


### Caracteristicas
- Listar todos os alunos, cursos e professores.
- Recuperar um aluno, curso ou professor por ID.
- Adicionar novos alunos, cursos ou professores.
- Atualizar detalhes de alunos, cursos ou professores existentes.
- Excluir alunos, cursos ou professores.


### EndPoints
**POST**http://127.0.0.1:8000/alunos/

**Resposta:**
json
{
  "status": "sucesso",
  "mensagem": "Aluno adicionado com sucesso.",
  "dados": {...}
}


**GET**(http://127.0.0.1:8000/alunos/)
Recupere os detalhes de um aluno usando seu ID único.

**Resposta:**
json
{
  "status": "sucesso",
  "mensagem": "Aluno recuperado com sucesso.",
  "dados": {...}
}



**PUT**http://127.0.0.1:8000/alunos/2
Atualize os detalhes de um aluno existente usando seu ID.
json
**Resposta:**
{
  "status": "sucesso",
  "mensagem": "Aluno atualizado com sucesso.",
  "dados": {...}
}


**DELETE**http://127.0.0.1:8000/alunos/1
Exclua um aluno pelo seu ID.

**Resposta:**
json
{
  "status": "sucesso",
  "mensagem": "Aluno excluído com sucesso.",
  "dados": {...}
}

**POST**http://127.0.0.1:8000/professores/

**Resposta**
json
{
  "status": "sucesso",
  "mensagem": "Professor adicionado com sucesso.",
  "dados": {...}
}

**GET**http://127.0.0.1:8000/professores/1

**Resposta**
json{
  "status": "sucesso",
  "mensagem": "Professor recuperado com sucesso.",
  "dados": {...}
}

**PUT**http://127.0.0.1:8000/professores/1

**Resposta**
json{
  "status": "sucesso",
  "mensagem": "Professor atualizado com sucesso.",
  "dados": {...}
}

**DELETE**http://127.0.0.1:8000/professores/1

**Resposta**
json
{
  "status": "sucesso",
  "mensagem": "Professor excluído com sucesso.",
  "dados": {...}
}

**POST**http://127.0.0.1:8000/alunos/

**Resposta**
json
{
  "status": "sucesso",
  "mensagem": "Curso adicionado com sucesso.",
  "dados": {...}
}

**GET**http://127.0.0.1:8000/cursos/

**Resposta**
json{
  "status": "sucesso",
  "mensagem": "Curso recuperado com sucesso.",
  "dados": {...}
}

**PUT**http://127.0.0.1:8000/cursos/101

**Resposta**
json{
  "status": "sucesso",
  "mensagem": "Curso atualizado com sucesso.",
  "dados": {...}
}

**DELETE**http://127.0.0.1:8000/cursos/101

**Resposta**
json
{
  "status": "sucesso",
  "mensagem": "Curso excluído com sucesso.",
  "dados": {...}
}

### O que é venv?
O venv é uma ferramenta integrada ao Python que permite criar ambientes virtuais. Um ambiente virtual isola pacotes e dependências de um projeto, evitando conflitos entre diferentes projetos em sua máquina.

**Comandos Úteis do venv:**
-python -m venv nome_do_ambiente

**Ativar o Ambiente Virtual :**
NO WINDOWS:
-nome_do_ambiente\Scripts\activate
LINUX:
-source nome_do_ambiente/bin/activate

**Instalar Dependências no Ambiente Virtual** 
-pip install fastapi uvicorn
-pip install -r requirements.txt

**Desativar o Ambiente Virtual**
deactivate

**Excluir um Ambiente Virtual**
rm -rf nome_do_ambiente


### Como Correr
Pré-requisitos
    -Python3.9 ou superior
    -Instalar dependências
**Passos**    
1. Clone este repositório:
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Crie e ative um ambiente virtual:
WINDOWS:
    python -m venv venv
    venv\Scripts\activate
LINUX:
    python3 -m venv venv
    source venv/bin/activate

3. Instalar dependências:
-pip install -r requirements.txt

4. Inicie o servidor de desenvolvimento:
-uvicorn main:app --reload

5. Acesse no navegador
Documentos da API (Swagger UI): http://127.0.0.1:8000/docs 📄
Redoc: http://127.0.0.1:8000/redoc 📚

## Postman
https://app.getpostman.com/join-team?invite_code=68d447020dfa6546adcb64115e9e48bf&target_code=4389a04a3be6ae4b6d1bbf3b253e6b32