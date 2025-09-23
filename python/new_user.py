def new_user():
    from sqlalchemy.orm import sessionmaker
    from banco import db
    from tabelas import Usuario


    Session = sessionmaker(bind=db())
    session = Session()


    novo_usuario = Usuario(nome = input('Digite seu nome: '),
    sobrenome = input('Digite seu sobrenome: '),
    email = input('Digite seu email: '),
    senha = input('Digite sua senha: '))

    session.add(novo_usuario)
    session.commit()

    print('Novo usuario cadastrado com sucesso')