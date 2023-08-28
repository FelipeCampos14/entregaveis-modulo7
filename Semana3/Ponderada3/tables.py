# Scripts com os modelos das tabelas

# Importações utilizadas
from sqlalchemy import Column, Integer, String
from base import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email}, password={self.password})>"