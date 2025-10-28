from sqlalchemy import create_engine
import numpy as np
from sqlalchemy import inspect, text


class Banco():
        def __init__(self, nome):
            self.nome = nome
            self.local = create_engine("sqlite:///banco_local/{}.db".format(self.nome), echo=False)
            self.insp = inspect(self.local)

        # Pegando os nomes das tabelas: 
        def nome_tabela(self):
            nomes_tabelas = self.insp.get_table_names()
            print('Tabelas no banco: ')
            for nomeT in nomes_tabelas:
                print(f" - {nomeT}")
        
        # Fazendo Acesso das Colunas e Linhas da Tabela: 
        def conexao(self):
            with self.local.connect() as conexao:
                resultado = conexao.execute(text("SELECT * FROM tabela_csv"))
            self.linhas = resultado.fetchall()
            self.colunas = resultado.keys()

        # Exibindo nome das colunas: 
        def nome_coluna(self):
            print('Colunas Listadas dentro da Tabela do Banco: ')
            for nomeC in self.colunas:
                print(f" - {nomeC}")

        # Transformando em Numpy array e exibindo o número de linhas e colunas do banco: 
        def array_numpy(self):
            self.data = np.array(self.linhas)
            print(f"\nNúmero de linhas e colunas: {self.data.shape}\n")


        # Exibe as arrays
        def exibir(self):
            for data_array in self.data:
                print(f"\n{data_array}")

        # Exibe os valores da primeira coluna e a contagem de ocorrencias:
        def ocorrencias(self):
            coluna = np.array([linha[0] for linha in self.linhas])
            valores, contagens = np.unique(coluna, return_counts=True)
            for val, oc in zip(valores, contagens):
                print(f"{val} → {oc} ocorrências")

