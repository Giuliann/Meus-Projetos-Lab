from sqlalchemy import create_engine
import numpy as np
from sqlalchemy import inspect, text


class Banco():
        # Inicio do Banco: 
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

        # Exibe as arrays: 
        def exibir(self):
            for data_array in self.data:
                print(f"\n{data_array}")

        # Exibe os valores da primeira coluna e a contagem de ocorrencias:
        def ocorrencias(self):
            coluna = np.array([linha[0] for linha in self.linhas])
            valores, contagens = np.unique(coluna, return_counts=True)
            for val, oc in zip(valores, contagens):
                print(f"{val} → {oc} ocorrências")
        
        # Exibe a media de desvios do paylaod e dos pacotes: 
        def media_e_desvio(self):
            # Media e desvio do paylaod: 
            paylaod = []
            for x in self.data[:, 45]:
                if x not in (None, '', 'None'):
                    paylaod.append(float(x))
                    try:
                        paylaod.append(float(x))
                    except ValueError:
                        continue

            media_payload = np.mean(paylaod) if paylaod else float('nan')
            desvio_payload = np.std(paylaod) if paylaod else float('nan')

            # Media e desvio dos pacotes: 
            pacotes = []
            for x in self.data[:, 22]:
                if x not in (None, '', 'None'):
                    try:
                        pacotes.append(float(x))
                    except ValueError:
                        continue

            media_pacote = np.mean(pacotes) if pacotes else float('nan')
            desvio_pacote = np.std(pacotes) if pacotes else float('nan')

            print(f'\n\nMedia do payload:{media_payload} e seu desvio{desvio_payload}\n\n')
            print(f'\n\nMedia do pacote:{media_pacote} e seu desvio{desvio_pacote}\n\n')

        # Exibe as alives, media entre os intervalos e a media de frquencia entre as alives
        def frequencia_alive(self):
            alive = [linha for linha in self.data if linha[48] in (12, 13)]

            if not alive:
                print('Pacote não encontrado')
                return
            
            tempo = sorted([float(linha[2]) for linha in alive])
            intervalo = np.diff(tempo)
            media_intevalo = np.mean(intervalo)
            frequencia = 1 / media_intevalo

            print(f'Alives encontradas: {len(alive)}')
            print(f'Media entre os intervalos: {media_intevalo:.6f} segundos')
            print(f'Media da frequencia: {frequencia:.6f} alive por segundo')



