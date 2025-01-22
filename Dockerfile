# Escolher a imagem base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . /app

# Instalar dependências necessárias (se houver um requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Instalar dependências do sistema para lidar com CSS e recursos estáticos
RUN apt-get update && apt-get install -y \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Configurar o comando que será executado ao iniciar o container
CMD ["python", "main.py"]  # Substitua "main.py" pelo seu arquivo de execução principal
