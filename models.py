from sqlalchemy import DATE, VARCHAR, CHAR, FLOAT, Enum, \
                        INTEGER, SMALLINT, BOOLEAN, ForeignKey
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

class Livro(Base):
    __tablename__ = "livro"
    id_livro: Mapped[int] = mapped_column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    preco: Mapped[float] = mapped_column(FLOAT, nullable=True)
    quantidade_estoque: Mapped[int] = mapped_column(INTEGER, nullable=False)
    quantidade_vendidas: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    data_publicacao: Mapped[date] = mapped_column(DATE, nullable=False)



class Metodo_pagamento(Base):
    __tablename__ = "metodo_pagamento"
    id_metodo_pagamento: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    parcelas: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    tipo: Mapped[str] = mapped_column(VARCHAR(7), nullable=False)

class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    login: Mapped[str] = mapped_column(VARCHAR(20), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    cpf: Mapped[int] = mapped_column(SMALLINT, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    quantidade_compras: Mapped[int] = mapped_column(SMALLINT, nullable=False, default=0)

class Avaliacao(Base):
    __tablename__ = "avaliacao"
    id_avaliacao: Mapped[int] = mapped_column(INTEGER, unique=True, autoincrement=True, nullable=False, primary_key=True)
    estrelas: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    avaliador: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro), nullable=False)
    cliente_id_cliente: Mapped[int] = mapped_column(INTEGER,ForeignKey(Cliente.id_cliente), nullable=False)
    

class Categoria(Base):
    __tablename__ = "categoria"
    id_categoria: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    classificacao_indicativa: Mapped[int] = mapped_column(SMALLINT, nullable=False)

class Editora(Base):
    __tablename__ = "editora"
    id_editora: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    exemplares_vendidos: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)

class Venda(Base):
    __tablename__ = "venda"
    id_venda: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    metodo_pagamento_id_metodo_pagamento: Mapped[int] = mapped_column(INTEGER,ForeignKey(Metodo_pagamento.id_metodo_pagamento), nullable=False)
    cliente_id_cliente: Mapped[int] = mapped_column(INTEGER,ForeignKey(Cliente.id_cliente), nullable=False)

class Livro_autores(Base):
    __tablename__ = "livro_has_autores"
    autor_id_autores: Mapped[int] = mapped_column(INTEGER,ForeignKey(Autores.id_autores), primary_key=True, nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro), primary_key=True, nullable=False)

class Livro_categoria(Base):
    __tablename__ = "livro_has_categoria"
    categoria_id_categoria: Mapped[int] = mapped_column(INTEGER,ForeignKey(Categoria.id_categoria), primary_key=True, nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro), primary_key=True, nullable=False)

class Livro_editora(Base):
    __tablename__ = "livro_has_editora"
    editora_id_editora: Mapped[int] = mapped_column(INTEGER,ForeignKey(Editora.id_editora), primary_key=True, nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro), primary_key=True, nullable=False)

class Livro_venda(Base):
    __tablename__ = "livro_has_venda"
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro), primary_key=True, nullable=False)
    venda_id_venda: Mapped[int] = mapped_column(INTEGER,ForeignKey(Venda.id_venda), primary_key=True, nullable=False)
    quantidade: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    preco: Mapped[float] = mapped_column(FLOAT, nullable=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)