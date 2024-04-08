from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote
from sqlalchemy_utils import database_exists, create_database


USER = "root"
PASSWD = quote("root")
HOST = "localhost" # 127.0.0.1
PORT = 3306
DATABASE = "Mr.Paper"

url = f'mysql+pymysql://{USER}:{PASSWD}@{HOST}:{PORT}/{DATABASE}'

if not database_exists(url=url):
    create_database(url=url)
    print(f"O banco de dados {DATABASE} foi criado com sucesso!!")
else:
    print(f"O banco de dados {DATABASE} já existe")

engine = create_engine(url=url, echo=True)
session = scoped_session(sessionmaker(bind=engine, autoflush=False))