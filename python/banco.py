def db():
    from sqlalchemy import create_engine

    db = create_engine("sqlite:///banco_local/meu_banco.db")
    return(db)