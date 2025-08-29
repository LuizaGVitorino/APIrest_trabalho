from fastapi import FastAPI
from app.models.database import engine, Base

# Crie a instância da API
app = FastAPI(
    title="API de Dados do Governo",
    version="0.1.0",
    description="API RESTful para consulta de dados públicos do portal dados.gov.br."
)

# Crie as tabelas no banco de dados
@app.on_event("startup")
def create_db_tables():
    Base.metadata.create_all(bind=engine)

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Dados do Governo! Acesse /docs para a documentação interativa."}
from fastapi import FastAPI
from app.models.database import engine, Base
from app.routes import auth

# Cria a API e o banco de dados
app = FastAPI(
    title="API de Dados do Governo",
    version="0.1.0",
    description="API RESTful para consulta de dados públicos do portal dados.gov.br."
)

# Inclua as rotas de autenticação
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])

# Crie as tabelas no banco de dados
@app.on_event("startup")
def create_db_tables():
    Base.metadata.create_all(bind=engine)

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Dados do Governo! Acesse /docs para a documentação interativa."}