# Importações utilizadas
from base import Base, engine
from tables import User

if __name__=="__main__":
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(engine)