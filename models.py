from sqlalchemy import DATE, VARCHAR, CHAR, Enum, \
                        INTEGER, SMALLINT, BOOLEAN, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import date
from connection import engine

class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = "pessoa"
    codigo: Mapped[int] = mapped_column('codigo', INTEGER, autoincrement=True, primary_key=True)
    email_institucional: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), primary_key=True)
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    data_nasc: Mapped[date] = mapped_column(DATE, nullable=False)
    email_pessoal: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    

class Filial(Base):
    __tablename__ = "filial"
    codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.codigo), primary_key=True)
    tipo: Mapped[str] = mapped_column(Enum("Centro Universitário", "Universidade", "Faculdade"), nullable=False)


class Escola(Base):
    __tablename__ = "escola"
    codigo_escola: Mapped[int] = mapped_column(SMALLINT, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    filial_codigo: Mapped[int] = mapped_column(INTEGER, ForeignKey(Filial.codigo), nullable=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)