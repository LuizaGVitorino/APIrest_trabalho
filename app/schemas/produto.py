from pydantic import BaseModel
from typing import Optional

# Schemas para Operadora
class OperadoraBase(BaseModel):
    nome: str
    razao_social: Optional[str] = None

class OperadoraCreate(OperadoraBase):
    pass

class Operadora(OperadoraBase):
    id: int

    class Config:
        from_attributes = True

# Schemas para Segmentacao
class SegmentacaoBase(BaseModel):
    tipo: str

class SegmentacaoCreate(SegmentacaoBase):
    pass

class Segmentacao(SegmentacaoBase):
    id: int

    class Config:
        from_attributes = True

# Schemas para Produto
class ProdutoBase(BaseModel):
    nome: str
    numero_registro: str
    tipo_cobertura: Optional[str] = None

class ProdutoCreate(ProdutoBase):
    operadora_id: int
    segmentacao_id: int

class Produto(ProdutoBase):
    id: int
    operadora: Operadora
    segmentacao: Segmentacao

    class Config:
        from_attributes = True