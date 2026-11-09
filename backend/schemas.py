
from pydantic import BaseModel, EmailStr, Field
from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    description: str = ""
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    low_stock_threshold: int = Field(default=5, ge=0)
    category: str = ""