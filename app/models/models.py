from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    """
    Modelo de usuário para autenticação.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

class Operadora(Base):
    """
    Representa a operadora do plano de saúde.
    """
    __tablename__ = "operadoras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    razao_social = Column(String)
    
    # Relação 1:N com Produto
    produtos = relationship("Produto", back_populates="operadora")

class Segmentacao(Base):
    """
    Representa a segmentação assistencial do produto (plano).
    """
    __tablename__ = "segmentacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, unique=True, index=True)
    
    # Relação 1:N com Produto
    produtos = relationship("Produto", back_populates="segmentacao")

class Produto(Base):
    """
    Representa um produto (plano de saúde).
    """
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    numero_registro = Column(String, unique=True, index=True)
    tipo_cobertura = Column(String)

    # Chaves estrangeiras para as entidades Operadora e Segmentacao
    operadora_id = Column(Integer, ForeignKey("operadoras.id"))
    segmentacao_id = Column(Integer, ForeignKey("segmentacoes.id"))
    
    # Relações com as outras tabelas
    operadora = relationship("Operadora", back_populates="produtos")
    segmentacao = relationship("Segmentacao", back_populates="produtos")