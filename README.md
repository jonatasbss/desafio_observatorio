# 📊 **Observatório da Indústria - API de Dados da PIA Empresa**  

## 📖 **Descrição do Projeto**  
Esta API foi desenvolvida para fornecer dados da **Pesquisa Industrial Anual - Empresa (PIA Empresa)** do IBGE, permitindo que aplicações frontend e mobile realizem consultas otimizadas e escaláveis. A API recebe requisições, processa parâmetros, consulta o banco de dados e retorna os dados de forma eficiente.  

O objetivo é garantir alta performance mesmo com grandes volumes de dados, oferecendo suporte a análises estatísticas e geração de relatórios para usuários cadastrados.  

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

### 🔹 **Passos**  

1. Clone este repositório:  
   ```sh
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
   ```  

2. Configure as variáveis de ambiente:  
   ```sh
   cp .env.example .env
   ```  
   Edite o `.env` e defina as credenciais corretas para o banco de dados e JWT.  

3. Suba os serviços com Docker:  
   ```sh
   docker-compose up --build
   ```  

4. A API estará disponível em:  
   👉 **http://localhost:8000**  

5. Documentação interativa via Swagger:  
   👉 **http://localhost:8000/docs**  

---

## 🔍 **Endpoints da API**  

### 📌 **Autenticação**  
- `POST /auth/login` → Login de usuário  
- `POST /auth/signup` → Cadastro de usuário  

### 📌 **Consulta de Dados**  
- `GET /dados?ano=2020&atividade=1001` → Retorna os dados filtrados  

### 📌 **Administração**  
- `POST /usuarios` → Criação de usuário (admin)  
- `DELETE /usuarios/{id}` → Remoção de usuário  

---

## 🔒 **Segurança**  
✅ **JWT** – Tokens seguros para controle de acesso.  
✅ **Rate Limit** – Limitação de requisições para evitar sobrecarga.  
✅ **CORS** – Proteção contra acessos não autorizados.  

---

## ✅ **Testes**  

Para rodar os testes unitários e de integração:  
```sh
pytest
```  

---

## 📄 **Licença**  
Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.  

---

### 🤝 **Contribuições**  
Sinta-se à vontade para abrir **issues** e enviar **pull requests**! 🚀

