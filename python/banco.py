def db():
    from sqlalchemy import create_engine

    # Banco de dados local:
    db = create_engine("sqlite:///banco_local/meu_banco.db")
    return(db)