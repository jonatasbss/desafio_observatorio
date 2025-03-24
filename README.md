# 📊 **Observatório da Indústria - API de Dados da PIA Empresa**

## 📖 **Descrição do Projeto**

Esta API foi desenvolvida para fornecer dados da **Pesquisa Industrial Anual - Empresa (PIA Empresa)** do IBGE,
permitindo que aplicações frontend e mobile realizem consultas otimizadas e escaláveis. A API recebe requisições,
processa parâmetros, consulta o banco de dados e retorna os dados de forma eficiente.

O objetivo é garantir alta performance mesmo com grandes volumes de dados, oferecendo suporte a análises estatísticas e
geração de relatórios para usuários cadastrados.

---

## 🚀 **Tecnologias Utilizadas**

- **Linguagem:** Python 3.11
- **Framework Backend:** FastAPI (escolhido pela sua alta performance e documentação automática)
- **Banco de Dados:** PostgreSQL (pela escalabilidade e robustez para grandes volumes de dados)
- **ORM:** SQLAlchemy
- **Cache:** Redis (para otimizar consultas frequentes)
- **Autenticação:** JWT (para controle de acesso seguro)
- **Containerização:** Docker + Docker Compose
- **Testes:** Pytest

---

## 📌 **Por que escolhi essas tecnologias?**

✅ **FastAPI** – Framework assíncrono e altamente performático, ideal para APIs escaláveis.  
✅ **PostgreSQL** – Banco de dados relacional otimizado para grandes volumes de dados.  
✅ **Redis** – Armazena consultas frequentes em cache, melhorando o tempo de resposta da API.  
✅ **Docker** – Facilita a distribuição e configuração do ambiente.

---

## ⚡ **Como Rodar o Projeto?**

### 🔹 **Pré-requisitos**

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.11](https://www.python.org/downloads/release/python-3119/)
- [Git](https://git-scm.com/downloads)

## 💻 Como Executar Localmente

### 1. Clone este repositório:

```
git clone {url_repository}
```  

### 2. Navegue até a pasta

```
cd {project_directory}
```

### 3. Criar e iniciar o ambiente virtual (Sistemas baseados em Unix)

```
python3 -m venv venv
source venv/bin/activate
```

### Ambiente Windows

### 3.1 - Pesquise na barra de pesquisa do menu iniciar por 'Windows PowerShell' e o execute como administrador. Quando abrir, execute o seguinte comando.

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 3.2 - Crie a virtualenv com o comando (Ambiente Windows)

```
python -m venv venv
.\venv\Scripts\activate
```

### 4 - Crie os arquivos .env (Ambiente Unix)

Baixe o arquivo [.env](https://drive.google.com/drive/folders/1LonhrR3TfTlHA_5GQym2avjwJUwTHe-M?usp=drive_link)

```
touch .env
```

### 4.1 - Crie os arquivos .env (Ambiente Windows)

```
type nul > .env
```

### 5 - Instale as bibliotecas

```
pip install -r requirements-dev.txt
```

### 6 - Alembic

O Alembic é uma ferramenta de migração para bancos de dados em projetos que utilizam SQLAlchemy. Ele permite gerenciar
versões do esquema do banco de dados, garantindo que todas as tabelas e colunas necessárias sejam criadas e atualizadas
corretamente. Baixe o
arquivo [alembic.ini](https://drive.google.com/drive/folders/1LonhrR3TfTlHA_5GQym2avjwJUwTHe-M?usp=drive_link)

Abra o arquivo alembic.ini e altere a linha passando a url com as credenciais corretas do banco ex.:

```
sqlalchemy.url = postgresql://user_observ:pass_observ@db:5432/empresa_pia
```

### 7 - Inicie o servidor

```
fastapi run apps/main.py
```

### 8 - A API estará disponível em:

👉 **http://0.0.0.0:8000**

### 9 - Documentação interativa via Swagger:

👉 **http://0.0.0.0:8000/docs**

---

## 💻 Como Executar no Docker

### 1 - Clone este repositório:

```
git clone {url_repository}
```  

### 2 - Navegue até a pasta

```
cd {project_directory}
```

### 3 - Suba os serviços com Docker:

```
docker-compose -f docker-compose.yml up -d --build
``` 

### 4 - Baixe o arquivo .env e alembic.ini e adicione ao projeto
Atente-se ao passar as credenciais contidas no arquivo docker-compose do banco de dados.

👉 **[Arquivos](https://drive.google.com/drive/folders/1LonhrR3TfTlHA_5GQym2avjwJUwTHe-M?usp=drive_link)**

### 5 - A API estará disponível em:

👉 **http://0.0.0.0:8002**

### 6 - Documentação interativa via Swagger:

👉 **http://0.0.0.0:8002/docs**

### 6 - Credenciais:

👉 **Email: admin@empresa.com**

👉 **Senha: admin123**

---

## 🔍 **Endpoints da API**

### 📌 **Autenticação**

- `POST /auth/login` → Login de usuário
- `POST /auth/logout` → Logout de usuário

### 📌 **Consulta de Dados**

- `GET /dados?atividade_economica_codigo_cnae=10.1&periodo_ano=2021` → Retorna os dados filtrados

### 📌 **Usuários**

- `POST /user/users` → Criação de usuário
- `DELETE  /user/users/{user_id}` → Remoção de usuário

---

## 🔒 **Segurança**

✅ **JWT** – Tokens seguros para controle de acesso.  
✅ **Rate Limit** – Limitação de requisições para evitar sobrecarga.  
✅ **CORS** – Proteção contra acessos não autorizados.

---

## ✅ **Testes**

Para rodar os testes unitários e de integração:

```
pytest
```  

---

## 📄 **Licença**

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

### 🤝 **Contribuições**

Sinta-se à vontade para abrir **issues** e enviar **pull requests**! 🚀

