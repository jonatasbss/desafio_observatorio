FROM python:3.11-slim

# Instalar dependências do sistema (caso necessário)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências primeiro (evita recriar as dependências se o código não mudar)
COPY requirements.txt /app/
COPY requirements-dev.txt /app/

# Criar o ambiente virtual
RUN python -m venv /env

# Instalar as dependências de produção
RUN /env/bin/pip install --no-cache-dir -r requirements.txt

# Instalar as dependências de desenvolvimento (incluindo pytest)
RUN /env/bin/pip install --no-cache-dir -r requirements-dev.txt

# Copiar o restante do código da aplicação
COPY . /app/

# Expor a porta que o FastAPI usará
EXPOSE 8001

# Comando para rodar a aplicação usando o Uvicorn
CMD ["/env/bin/uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
