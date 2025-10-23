def vizu():
    from banco import db
    import numpy as np
    from sqlalchemy import inspect, text

    # Acessando o banco: 
    banco = db()
    insp = inspect(banco)

    # Pegando os nomes das tabelas: 
    nomes_tabelas = insp.get_table_names()
    print('Tabelas no banco: ')
    for nomeT in nomes_tabelas:
        print(f" - {nomeT}")

    # Fazendo Acesso das Colunas e Linhas da Tabela:  
    with banco.connect() as conexao:
        resultado = conexao.execute(text("SELECT * FROM tabela_csv"))
        linhas = resultado.fetchall()
        colunas = resultado.keys()

    # Lista com os nomes das colunas da Tabela: 
    print('Colunas Listadas dentro da Tabela do Banco: ')
    for nomeC in colunas:
        print(f" - {nomeC}")

    print("\n\nPrimeiras linhas:\n",linhas[:1])

    # Pra as informaçôes não sumirem do terminal: 
    input("\nPressione ENTER para ver as ocorrências...")

    # Transformando em Numpy
    data = np.array(linhas)
    print(f"\nNúmero de linhas e colunas: {data.shape}\n")

    # Exibe as arrays
    for data_array in data:
        print(f"\n{data_array}")

    coluna = np.array([linha[0] for linha in linhas])
    print('Array NumPy:', coluna)

    # Exibe os valores da lista e a contagem de ocorrencias: 
    valores, contagens = np.unique(coluna, return_counts=True)
    for val, oc in zip(valores, contagens):
        print(f"{val} → {oc} ocorrências")

    