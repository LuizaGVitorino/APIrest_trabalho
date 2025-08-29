from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    """
    Schema base para os dados do usuário.
    """
    username: str

class UserCreate(UserBase):
    """
    Schema para a criação de um novo usuário.
    """
    password: str

class User(UserBase):
    """
    Schema para retornar os dados do usuário.
    """
    id: int
    is_admin: bool = Field(default=False)

    class Config:
        from_attributes = True

class Token(BaseModel):
    """
    Schema para o token JWT.
    """
    access_token: str
    token_type: str