def vizu():
    from banco import db
    import numpy as np
    from sqlalchemy import inspect, text

    # Exibe os nomes das tabelas existentes do banco.
    insp = inspect(db())
    tabelas = insp.get_table_names()
    print('Tabelas no banco:', tabelas)

    # Faz conexão com o banco local, pegas as linhas da tabela e mostra elas.
    with db().connect() as conexao:
        resultado = conexao.execute(text("SELECT * FROM usuarios"))
        linhas = resultado.fetchall()

    # pra evitar poluição.
    print('Primeiras linhas:', linhas[:5])

    # conversão pra numpy.
    coluna = np.array([linha[0] for linha in linhas])
    print('Array NumPy:', coluna)

    # Contar a frequência de cada valor em uma coluna.
    valores, contagens = np.unique(coluna, return_counts=True)
    for v, c in zip(valores, contagens):
        print(f"{v} → {c} ocorrências")