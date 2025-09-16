def vizu():
    from banco import db
    import numpy as np
    from sqlalchemy import inspect, text

    insp = inspect(db())
    tabelas = insp.get_table_names()
    print('Tabelas no banco:', tabelas)

    # Faz conexão com o banco local, pegas as linhas da tabela e mostra elas
    with db().connect() as conexao:
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