
# Adicione essas importações no topo do arquivo auth.py
from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError
from app.models.models import User
from app.models.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

# Configuração para o esquema de autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Verifica a validade do token e retorna o usuário associado.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decodifica o token para obter o nome de usuário
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Busca o usuário no banco de dados
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
        
    return user
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configurações de segurança
SECRET_KEY = "computacao8"  # Mude esta chave!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Verifica se a senha em texto puro corresponde ao hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Cria um hash para a senha."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Cria um token de acesso JWT."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt