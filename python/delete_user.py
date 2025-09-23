def delete():
    from sqlalchemy.orm import sessionmaker
    from tabelas import Usuario
    from banco import db


    Session = sessionmaker(bind=db())
    session = Session()


    id_usuario = int(input("Digite o ID do Usuario a deletar: "))


    usuario = session.query(Usuario).filter_by(id=id_usuario).first()

    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuario com id {} deletado com sucesso!".format(id_usuario))
    else:
        print("Usuario não encontrado.")