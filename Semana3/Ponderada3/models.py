from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id : int = Field(default=None, gt=0)
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)