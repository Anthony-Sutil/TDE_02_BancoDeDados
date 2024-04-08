from sqlalchemy import DATE, VARCHAR, CHAR, Enum, \
                        INTEGER, SMALLINT, TINYINT, BOOLEAN, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import date
from connection import engine

class Base(DeclarativeBase):
    pass


class autores(Base):
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
    

class Filial(Base):
    __tablename__ = "filial"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(autores.id_autores), primary_key=True)
    tipo: Mapped[str] = mapped_column(Enum("Centro Universitário", "Universidade", "Faculdade"), nullable=False)


class Escola(Base):
    __tablename__ = "escola"
    codigo_escola: Mapped[int] = mapped_column(SMALLINT, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    filial_codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Filial.codigo), nullable=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)