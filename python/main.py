# Imports importantes
from sqlalchemy import create_engine, inspect, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import numpy as np

# Criando uma ponte entre o banco de dados e meu codigo, criei banco local prs teste.
db = create_engine("sqlite:///banco_local/meu_banco.db")

# Declarando a sessão
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Tabela Usuario

class Usuario(Base):
	__tablename__ = 'usuarios'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	nome = Column(String)
	sobrenome = Column(String)
	email = Column(String)
	senha =Column(String)
	
	def __init__(self, nome,sobrenome, email, senha):
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
		self.senha = senha

#Tabela Equipes

class Equipe(Base):
	__tablename__ = 'equipes'
			
	id = Column(Integer, primary_key=True, autoincrement=True)
	nome_equipe = Column(String)
	funcao_equipe = Column(String)

	def __init__(self, nome_equipe, funcao_equipe):
		self.nome_equipe = nome_equipe
		self.funcao_equipe = funcao_equipe



Base.metadata.create_all(bind=db)


novo_usuario = Usuario(nome = input('Digite seu nome: '),
sobrenome = input('Digite seu sobrenome: '),
email = input('Digite seu email: '),
senha = input('Digite sua senha: '))

session.add(novo_usuario)
session.commit()

nova_equipe = Equipe(nome_equipe = input('Digite nome da equipe: '),
funcao_equipe = input('Digite a função da equipe: '))

session.add(nova_equipe)
session.commit()

# Inspeciona o banco de dados e mosta os nomes das tabelas do banco.
insp = inspect(db)
tabelas = insp.get_table_names()
print('Tabelas no banco:', tabelas)

# Faz conexão com o banco local, pegas as linhas da tabela e mostra elas
with db.connect() as conexao:
    resultado = conexao.execute(text("SELECT * FROM usuarios"))
    linhas = resultado.fetchall()

print('Primeiras linhas:', linhas[:5])
# pra evitar poluição

coluna = np.array([linha[0] for linha in linhas])
print('Array NumPy:', coluna)
# conversão pra numpy

valores, contagens = np.unique(coluna, return_counts=True)
for v, c in zip(valores, contagens):
    print(f"{v} → {c} ocorrências")
#aqui aontece a contagem de ocorrencias 