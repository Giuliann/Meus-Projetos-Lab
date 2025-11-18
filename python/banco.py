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

        # Exibe as alives, media entre os intervalos e a media de frquencia entre as alives:
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
        
        # Exibe e media e desvio dos tamanho dos topicos 'Publish' e 'Subscribe':
        def media_desvio_topico(self):
            publish = []
            subscribs = []
            
            for linha in self.data:
                msgttype = linha[48]
                topico = linha[57]
                if topico in('None', '', None):
                    continue
            
            tamanho = len(str(topico))
            if msgttype == 3:
                publish.append(tamanho)
            if msgttype == 8:
                subscribs.append(tamanho)

            media_pub = np.mean(publish) if publish else 0
            desvio_pub = np.std(publish) if publish else 0

            media_sub = np.mean(subscribs) if subscribs else 0
            desvio_sub = np.std(subscribs) if subscribs else 0

            print('Media e desvio dos topicos')
            print(f'Publish media: {media_pub:.2f} e desvio: {desvio_pub:.2f}')
            print(f'Subscribe media: {media_sub:.2f} e desvio: {desvio_sub:.2f}')

        # Conta e exibe as mensagens 'QOS 1', 'QOS 2' e 'QOS 3':
        def distribuição_msg_QOS(self):
            qos1 = 0
            qos2 = 0
            qos3 = 0

            for linha in self.data:
                qos = linha[53]

                if qos in ('None', '', None):
                    continue

                try:
                    qos = int(float(qos))
                except:
                    continue

                if qos == 0:
                    qos1 = qos1 + 1

                elif qos == 1:
                    qos2 = qos2 + 1

                elif qos == 2:
                    qos3 = qos3 + 1

            total = qos1 + qos2 + qos3

            print('Mensagens QOS: ')
            print(f'QOS 1: {qos1} mensagens ({(qos1/total)*100:.2f}%)')
            print(f'QOS 2: {qos2} mensagens ({(qos2/total)*100:.2f}%)')
            print(f'QOS 3: {qos3} mensagens ({(qos3/total)*100:.2f}%)')
            print(f'Mensagens totais: {total}')

        # Exibe o tempo entre o primeiro e ultimo pacote:
        def temp_pacotes(self):
            tempos = []
            for linha in self.data:
                 tempo = linha[2]
                 if tempo not in ('None', '', None):
                    try:
                        tempos.append(float(tempo))
                    except:
                        continue

            # menssagem de erro:
            if len(tempos) < 2:
                print('Não existe tempo suficiente para calcular duração')
                return
            
            inicio = min(tempos)
            fim = max(tempos)
            duracao = fim - inicio

            print(f'Tempo total da conexão: {duracao:.2f} segundos')
            print(f'Inicio da conexão: {inicio}')
            print(f'Fim da conexão: {fim}')

        # Exibe a proporção de pacotes de entrada/saida: 
        def proporcao_entrada_saida(self):
            client_ip  = self.data[0][5]

            entrada = 0
            saida = 0

            for linha in self.data:
                src = linha[5]
                dst = linha[6]

                if dst == client_ip:
                    entrada = entrada + 1

                elif src == client_ip:
                    saida = saida + 1

            total = entrada + saida
            if total == 0:
                # menssagem de erro:
                print('Não da pra efetuar o calculo')
                return
            
            # porcentagem dos pacotes:
            prop_entrada = entrada / total*100
            prop_saida = saida / total*100

            print(f'IP do cliente: {client_ip}')
            print(f'Entrada dos pacotes {entrada} ({prop_entrada:.2f}%)')
            print(f'Saida dos pacotes {saida} ({prop_saida:.2f}%)')
            print(f'Total de pacotes analisados: {total} pacotes')
                

            