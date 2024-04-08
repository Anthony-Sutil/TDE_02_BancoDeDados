from sqlalchemy import DATE, VARCHAR, CHAR, FLOAT, Enum, \
                        INTEGER, SMALLINT, TINYINT, BOOLEAN, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import date
from connection import engine

class Base(DeclarativeBase):
    pass


class Autores(Base):
    __tablename__ = "autores"
    id_autores: Mapped[int] = mapped_column('id_autores', INTEGER, autoincrement=True, nullable=False, primary_key=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    data_nascimento: Mapped[date] = mapped_column(DATE, nullable=False)
    biografia: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)

class Avaliacao(Base):
    __tablename__ = "avaliacao"
    id_avaliacao: Mapped[int] = mapped_column(INTEGER, unique=True, autoincrement=True, nullable=False, primary_key=True)
    estrelas: Mapped[int] = mapped_column(TINYINT, nullable=False, unsigned=True)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    avaliador: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(livro.id_livro), nullable=False)
    cliente_id_cliente: Mapped[int] = mapped_column(INTEGER,ForeignKey(cliente.id_cliente), nullable=False)
    

class Categoria(Base):
    __tablename__ = "categoria"
    id_categoria: Mapped[int] = mapped_column(INTEGER, primary_key=True, unsigned=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    classificacao_indicativa: Mapped[int] = mapped_column(TINYINT, nullable=False, unsigned=True)


class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    login: Mapped[str] = mapped_column(VARCHAR(20), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    cpf: Mapped[int] = mapped_column(TINYINT, nullable=False, unsigned=True)
    email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    quantidade_compras: Mapped[int] = mapped_column(SMALLINT, nullable=False, default=0)

class Editora(Base):
    __tablename__ = "editora"
    id_editora: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    exemplares_vendidos: Mapped[int] = mapped_column(SMALLINT, nullable=False, default=0)

class Livro(Base):
    __tablename__ = "livro"
    id_livro: Mapped[int] = mapped_column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    preco: Mapped[float] = mapped_column(FLOAT, unsigned=True, nullable=True)
    quantidade_estoque: Mapped[int] = mapped_column(INTEGER, unsigned=True, nullable=False)
    quantidade_vendidas: Mapped[int] = mapped_column(SMALLINT, unsigned=True, nullable=False)
    data_publicacao: Mapped[date] = mapped_column(DATE, nullable=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)