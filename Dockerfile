# Use uma imagem base com Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o container
COPY requirements.txt .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação
COPY . .

# Expõe a porta onde a aplicação FastAPI vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
