from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from banco import db

# Cria uma sessão

Session = sessionmaker(bind=db())
session = Session()

Base = declarative_base()

# Tabela de Usuarios:

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    sobrenome = Column(String)
    email = Column(String)
    senha = Column(String)

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# Tabela da Equipes:

class Equipe(Base):
	__tablename__ = 'equipes'
			
	id = Column(Integer, primary_key=True, autoincrement=True)
	nome_equipe = Column(String)
	funcao_equipe = Column(String)

	def __init__(self, nome_equipe, funcao_equipe):
		self.nome_equipe = nome_equipe
		self.funcao_equipe = funcao_equipe


# Crie todas as tabelas definidas.
Base.metadata.create_all(bind=db())
