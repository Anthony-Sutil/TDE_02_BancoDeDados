from sqlalchemy import DATE, VARCHAR, CHAR, FLOAT, Enum, \
                        INTEGER, SMALLINT, BOOLEAN, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session
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
    @classmethod
    def buscar_por_nome(cls, nome):
        return session.query(cls).filter(cls.nome == nome).all()

class Livro(Base):
    __tablename__ = "livro"
    id_livro: Mapped[int] = mapped_column(INTEGER, primary_key=True,nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    preco: Mapped[float] = mapped_column(FLOAT, nullable=True)
    quantidade_estoque: Mapped[int] = mapped_column(INTEGER, nullable=False)
    quantidade_vendidas: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    data_publicacao: Mapped[date] = mapped_column(DATE, nullable=False)
    @classmethod
    def buscar_por_id(cls, id_livro):
        return session.query(cls).get(id_livro)



class Metodo_pagamento(Base):
    __tablename__ = "metodo_pagamento"
    id_metodo_pagamento: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    parcelas: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    tipo: Mapped[str] = mapped_column(VARCHAR(7), nullable=False)
    @classmethod
    def buscar_por_tipo(cls, tipo):
        return session.query(cls).filter(cls.tipo == tipo).all()

class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    login: Mapped[str] = mapped_column(VARCHAR(20), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    cpf: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    quantidade_compras: Mapped[int] = mapped_column(SMALLINT, nullable=False, default=0)
    @classmethod
    def buscar_por_email(cls, email):
        return session.query(cls).filter(cls.email == email).all()

class Avaliacao(Base):
    __tablename__ = "avaliacao"
    id_avaliacao: Mapped[int] = mapped_column(INTEGER, autoincrement=True, nullable=False, primary_key=True)
    estrelas: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    avaliador: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro, ondelete="CASCADE"), nullable=False)
    cliente_id_cliente: Mapped[int] = mapped_column(INTEGER,ForeignKey(Cliente.id_cliente, ondelete="CASCADE"), nullable=False)
    @classmethod
    def buscar_por_estrelas(cls, estrelas):
        return session.query(cls).filter(cls.estrelas == estrelas).all()

class Categoria(Base):
    __tablename__ = "categoria"
    id_categoria: Mapped[int] = mapped_column(INTEGER, primary_key=True,nullable=False, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    classificacao_indicativa: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    @classmethod
    def buscar_por_nome(cls, nome):
        return session.query(cls).filter(cls.nome == nome).all()

class Editora(Base):
    __tablename__ = "editora"
    id_editora: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    exemplares_vendidos: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)
    @classmethod
    def buscar_por_exemplares_vendidos(cls, exemplares_vendidos):
        return session.query(cls).filter(cls.exemplares_vendidos == exemplares_vendidos).all()

class Venda(Base):
    __tablename__ = "venda"
    id_venda: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    data: Mapped[date] = mapped_column(DATE, nullable=False)
    metodo_pagamento_id_metodo_pagamento: Mapped[int] = mapped_column(INTEGER,ForeignKey(Metodo_pagamento.id_metodo_pagamento, ondelete="CASCADE"), nullable=False)
    cliente_id_cliente: Mapped[int] = mapped_column(INTEGER,ForeignKey(Cliente.id_cliente, ondelete="CASCADE"), nullable=False)
    @classmethod
    def buscar_por_data(cls, data):
        return session.query(cls).filter(cls.data == data).all()

class Livro_autores(Base):
    __tablename__ = "livro_has_autores"
    autor_id_autores: Mapped[int] = mapped_column(INTEGER,ForeignKey(Autores.id_autores, ondelete="CASCADE"), primary_key=True, nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro, ondelete="CASCADE"), primary_key=True, nullable=False)
    @classmethod
    def buscar_por_autor_id(cls, autor_id):
        return session.query(cls).filter(cls.autor_id_autores == autor_id).all()

class Livro_categoria(Base):
    __tablename__ = "livro_has_categoria"
    categoria_id_categoria: Mapped[int] = mapped_column(INTEGER,ForeignKey(Categoria.id_categoria, ondelete="CASCADE"), primary_key=True, nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro, ondelete="CASCADE"), primary_key=True, nullable=False)
    def buscar_por_categoria_id(cls, categoria_id):
        return session.query(cls).filter(cls.categoria_id_categoria == categoria_id).all()

class Livro_editora(Base):
    __tablename__ = "livro_has_editora"
    editora_id_editora: Mapped[int] = mapped_column(INTEGER,ForeignKey(Editora.id_editora, ondelete="CASCADE"), primary_key=True, nullable=False)
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro, ondelete="CASCADE"), primary_key=True, nullable=False)
    @classmethod
    def buscar_por_editora_id(cls, editora_id):
        return session.query(cls).filter(cls.editora_id_editora == editora_id).all()

class Livro_venda(Base):
    __tablename__ = "livro_has_venda"
    livro_id_livro: Mapped[int] = mapped_column(INTEGER,ForeignKey(Livro.id_livro, ondelete="CASCADE"), primary_key=True, nullable=False)
    venda_id_venda: Mapped[int] = mapped_column(INTEGER,ForeignKey(Venda.id_venda, ondelete="CASCADE"), primary_key=True, nullable=False)
    quantidade: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    preco: Mapped[float] = mapped_column(FLOAT, nullable=False)
    @classmethod
    def buscar_por_quantidade(cls, quantidade):
        return session.query(cls).filter(cls.quantidade == quantidade).all()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)




# Cria uma nova sessão
session = Session(bind=engine)

# Inserir registros na tabela 'autores'
autores = [
    Autores(nome="Autor 1", data_nascimento=date(1970, 1, 1), biografia="Biografia do Autor 1"),
    Autores(nome="Autor 2", data_nascimento=date(1980, 2, 2), biografia="Biografia do Autor 2"),
    Autores(nome="Autor 3", data_nascimento=date(1990, 3, 3), biografia="Biografia do Autor 3"),
    Autores(nome="Autor 4", data_nascimento=date(1960, 4, 4), biografia="Biografia do Autor 4"),
    Autores(nome="Autor 5", data_nascimento=date(1950, 5, 5), biografia="Biografia do Autor 5"),
    Autores(nome="Autor 6", data_nascimento=date(2000, 6, 6), biografia="Biografia do Autor 6")
]
session.add_all(autores)
session.commit()

# Inserir registros na tabela 'livro'
livros = [
    Livro(nome="Livro 1", preco=100.0, quantidade_estoque=50, quantidade_vendidas=20, data_publicacao=date(2000, 1, 1)),
    Livro(nome="Livro 2", preco=150.0, quantidade_estoque=30, quantidade_vendidas=15, data_publicacao=date(2001, 2, 2)),
    Livro(nome="Livro 3", preco=200.0, quantidade_estoque=20, quantidade_vendidas=10, data_publicacao=date(2002, 3, 3)),
    Livro(nome="Livro 4", preco=250.0, quantidade_estoque=10, quantidade_vendidas=5, data_publicacao=date(2003, 4, 4)),
    Livro(nome="Livro 5", preco=300.0, quantidade_estoque=40, quantidade_vendidas=25, data_publicacao=date(2004, 5, 5)),
    Livro(nome="Livro 6", preco=350.0, quantidade_estoque=60, quantidade_vendidas=30, data_publicacao=date(2005, 6, 6))
]
session.add_all(livros)
session.commit()

# Inserir registros na tabela 'metodo_pagamento'
metodos_pagamento = [
    Metodo_pagamento(parcelas=1, tipo="Crédito"),
    Metodo_pagamento(parcelas=2, tipo="Débito"),
    Metodo_pagamento(parcelas=3, tipo="Pix"),
    Metodo_pagamento(parcelas=4, tipo="Dinheiro"),
    Metodo_pagamento(parcelas=5, tipo="Boleto"),
    Metodo_pagamento(parcelas=6, tipo="Cheque")
]
session.add_all(metodos_pagamento)
session.commit()

# Inserir registros na tabela 'cliente'
clientes = [
    Cliente(nome="Cliente 1", login="cliente1", senha="senha1", cpf=123456, email="cliente1@example.com"),
    Cliente(nome="Cliente 2", login="cliente2", senha="senha2", cpf=123457, email="cliente2@example.com"),
    Cliente(nome="Cliente 3", login="cliente3", senha="senha3", cpf=123458, email="cliente3@example.com"),
    Cliente(nome="Cliente 4", login="cliente4", senha="senha4", cpf=123459, email="cliente4@example.com"),
    Cliente(nome="Cliente 5", login="cliente5", senha="senha5", cpf=123460, email="cliente5@example.com"),
    Cliente(nome="Cliente 6", login="cliente6", senha="senha6", cpf=123461, email="cliente6@example.com")
]
session.add_all(clientes)
session.commit()

# Inserir registros na tabela 'avaliacao'
avaliacoes = [
    Avaliacao(estrelas=5, data=date(2023, 1, 1), avaliador="Avaliador 1", livro_id_livro=1, cliente_id_cliente=1),
    Avaliacao(estrelas=4, data=date(2023, 2, 2), avaliador="Avaliador 2", livro_id_livro=2, cliente_id_cliente=2),
    Avaliacao(estrelas=3, data=date(2023, 3, 3), avaliador="Avaliador 3", livro_id_livro=3, cliente_id_cliente=3),
    Avaliacao(estrelas=5, data=date(2023, 4, 4), avaliador="Avaliador 4", livro_id_livro=4, cliente_id_cliente=4),
    Avaliacao(estrelas=2, data=date(2023, 5, 5), avaliador="Avaliador 5", livro_id_livro=5, cliente_id_cliente=5),
    Avaliacao(estrelas=1, data=date(2023, 6, 6), avaliador="Avaliador 6", livro_id_livro=6, cliente_id_cliente=6)
]
session.add_all(avaliacoes)
session.commit()

# Inserir registros na tabela 'categoria'
categorias = [
    Categoria(nome="Ficção", classificacao_indicativa=12),
    Categoria(nome="Não Ficção", classificacao_indicativa=10),
    Categoria(nome="Romance", classificacao_indicativa=14),
    Categoria(nome="Tecnologia", classificacao_indicativa=16),
    Categoria(nome="História", classificacao_indicativa=10),
    Categoria(nome="Ciência", classificacao_indicativa=16)
]
session.add_all(categorias)
session.commit()

# Inserir registros na tabela 'editora'
editoras = [
    Editora(data=date(2020, 1, 1), nome="Editora A", exemplares_vendidos=500),
    Editora(data=date(2019, 2, 2), nome="Editora B", exemplares_vendidos=300),
    Editora(data=date(2018, 3, 3), nome="Editora C", exemplares_vendidos=200),
    Editora(data=date(2017, 4, 4), nome="Editora D", exemplares_vendidos=400),
    Editora(data=date(2016, 5, 5), nome="Editora E", exemplares_vendidos=600),
    Editora(data=date(2015, 6, 6), nome="Editora F", exemplares_vendidos=700)
]
session.add_all(editoras)
session.commit()

# Inserir registros na tabela 'venda'
vendas = [
    Venda(data=date(2023, 1, 1), metodo_pagamento_id_metodo_pagamento=1, cliente_id_cliente=1),
    Venda(data=date(2023, 2, 2), metodo_pagamento_id_metodo_pagamento=2, cliente_id_cliente=2),
    Venda(data=date(2023, 3, 3), metodo_pagamento_id_metodo_pagamento=3, cliente_id_cliente=3),
    Venda(data=date(2023, 4, 4), metodo_pagamento_id_metodo_pagamento=4, cliente_id_cliente=4),
    Venda(data=date(2023, 5, 5), metodo_pagamento_id_metodo_pagamento=5, cliente_id_cliente=5),
    Venda(data=date(2023, 6, 6), metodo_pagamento_id_metodo_pagamento=6, cliente_id_cliente=6)
]
session.add_all(vendas)
session.commit()

# Inserir registros na tabela 'livro_autores'
livro_autores = [
    Livro_autores(autor_id_autores=1, livro_id_livro=1),
    Livro_autores(autor_id_autores=2, livro_id_livro=2),
    Livro_autores(autor_id_autores=3, livro_id_livro=3),
    Livro_autores(autor_id_autores=4, livro_id_livro=4),
    Livro_autores(autor_id_autores=5, livro_id_livro=5),
    Livro_autores(autor_id_autores=6, livro_id_livro=6)
]
session.add_all(livro_autores)
session.commit()

# Inserir registros na tabela 'livro_categoria'
livro_categorias = [
    Livro_categoria(categoria_id_categoria=1, livro_id_livro=1),
    Livro_categoria(categoria_id_categoria=2, livro_id_livro=2),
    Livro_categoria(categoria_id_categoria=3, livro_id_livro=3),
    Livro_categoria(categoria_id_categoria=4, livro_id_livro=4),
    Livro_categoria(categoria_id_categoria=5, livro_id_livro=5),
    Livro_categoria(categoria_id_categoria=6, livro_id_livro=6)
]
session.add_all(livro_categorias)
session.commit()

# Inserir registros na tabela 'livro_editora'
livro_editoras = [
    Livro_editora(editora_id_editora=1, livro_id_livro=1),
    Livro_editora(editora_id_editora=2, livro_id_livro=2),
    Livro_editora(editora_id_editora=3, livro_id_livro=3),
    Livro_editora(editora_id_editora=4, livro_id_livro=4),
    Livro_editora(editora_id_editora=5, livro_id_livro=5),
    Livro_editora(editora_id_editora=6, livro_id_livro=6)
]
session.add_all(livro_editoras)
session.commit()

# Inserir registros na tabela 'livro_venda'
livro_vendas = [
    Livro_venda(livro_id_livro=1, venda_id_venda=1, quantidade=2, preco=100.0),
    Livro_venda(livro_id_livro=2, venda_id_venda=2, quantidade=3, preco=150.0),
    Livro_venda(livro_id_livro=3, venda_id_venda=3, quantidade=1, preco=200.0),
    Livro_venda(livro_id_livro=4, venda_id_venda=4, quantidade=4, preco=250.0),
    Livro_venda(livro_id_livro=5, venda_id_venda=5, quantidade=2, preco=300.0),
    Livro_venda(livro_id_livro=6, venda_id_venda=6, quantidade=3, preco=350.0)
]
session.add_all(livro_vendas)
session.commit()

# Atualizar registros na tabela Cliente
clientes_para_atualizar = session.query(Cliente).filter(Cliente.id_cliente <= 5).all()
for cliente in clientes_para_atualizar:
    cliente.quantidade_compras += 1

# Atualizar registros na tabela Livro
livros_para_atualizar = session.query(Livro).filter(Livro.id_livro <= 5).all()
for livro in livros_para_atualizar:
    livro.quantidade_estoque -= 10
    livro.preco += 5.00

# Atualizar registros na tabela Autores
autores_para_atualizar = session.query(Autores).filter(Autores.id_autores <= 5).all()
for autor in autores_para_atualizar:
    autor.biografia = f"Biografia atualizada do {autor.nome}"

# Atualizar registros na tabela Metodo_pagamento
metodos_pagamento_para_atualizar = session.query(Metodo_pagamento).filter(Metodo_pagamento.id_metodo_pagamento <= 5).all()
for metodo_pagamento in metodos_pagamento_para_atualizar:
    metodo_pagamento.parcelas += 1

# Atualizar registros na tabela Editora
editoras_para_atualizar = session.query(Editora).filter(Editora.id_editora <= 5).all()
for editora in editoras_para_atualizar:
    editora.exemplares_vendidos += 100

# Confirmar as atualizações na sessão
session.commit()




# Excluir um registro da tabela Avaliacao
avaliacao_para_excluir = session.query(Avaliacao).filter(Avaliacao.id_avaliacao == 1).one()
session.delete(avaliacao_para_excluir)

# Excluir um registro da tabela Livro
livro_para_excluir = session.query(Livro).filter(Livro.id_livro == 1).one()
session.delete(livro_para_excluir)

# Excluir um registro da tabela Metodo_pagamento
metodo_pagamento_para_excluir = session.query(Metodo_pagamento).filter(Metodo_pagamento.id_metodo_pagamento == 1).one()
session.delete(metodo_pagamento_para_excluir)

# Excluir um registro da tabela Cliente
cliente_para_excluir = session.query(Cliente).filter(Cliente.id_cliente == 1).one()
session.delete(cliente_para_excluir)

# Excluir um registro da tabela Categoria
categoria_para_excluir = session.query(Categoria).filter(Categoria.id_categoria == 1).one()
session.delete(categoria_para_excluir)

# Confirmar as exclusões na sessão
session.commit()


def consultar_dados():
    # Consulta 1: Buscar autores pelo nome
    autores_por_nome = Autores.buscar_por_nome("Autor 1")
    print("Autores encontrados pelo nome 'Autor 1':")
    for autor in autores_por_nome:
        print(f"ID: {autor.id_autores}, Nome: {autor.nome}")

    # Consulta 2: Buscar livro pelo ID
    livro_por_id = Livro.buscar_por_id(2)
    print("\nLivro encontrado pelo ID 2:")
    print(f"ID: {livro_por_id.id_livro}, Nome: {livro_por_id.nome}")

    # Consulta 3: Buscar método de pagamento pelo tipo
    metodo_pagamento_por_tipo = Metodo_pagamento.buscar_por_tipo("Crédito")
    print("\nMétodo de pagamento encontrado pelo tipo 'Crédito':")
    for metodo in metodo_pagamento_por_tipo:
        print(f"ID: {metodo.id_metodo_pagamento}, Tipo: {metodo.tipo}")

    # Consulta 4: Buscar cliente pelo email
    cliente_por_email = Cliente.buscar_por_email("cliente3@example.com")
    print("\nCliente encontrado pelo email 'cliente3@example.com':")
    for cliente in cliente_por_email:
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}")

    # Consulta 5: Buscar avaliações por estrelas
    avaliacoes_por_estrelas = Avaliacao.buscar_por_estrelas(5)
    print("\nAvaliações encontradas com 5 estrelas:")
    for avaliacao in avaliacoes_por_estrelas:
        print(f"ID: {avaliacao.id_avaliacao}, Estrelas: {avaliacao.estrelas}")

    # Consulta 6: Buscar categorias pelo nome
    categorias_por_nome = Categoria.buscar_por_nome("Ficção")
    print("\nCategorias encontradas pelo nome 'Ficção':")
    for categoria in categorias_por_nome:
        print(f"ID: {categoria.id_categoria}, Nome: {categoria.nome}")

    # Consulta 7: Buscar editoras pelo número de exemplares vendidos
    editoras_por_exemplares = Editora.buscar_por_exemplares_vendidos(600)
    print("\nEditoras encontradas com 600 exemplares vendidos:")
    for editora in editoras_por_exemplares:
        print(f"ID: {editora.id_editora}, Nome: {editora.nome}")

    # Consulta 8: Buscar vendas por data
    vendas_por_data = Venda.buscar_por_data(date(2023, 2, 2))
    print("\nVendas encontradas na data '2023-02-02':")
    for venda in vendas_por_data:
        print(f"ID: {venda.id_venda}, Data: {venda.data}")

    # Consulta 9: Buscar livros por autor ID
    livros_por_autor_id = Livro_autores.buscar_por_autor_id(3)
    print("\nLivros encontrados pelo ID do autor 3:")
    for livro in livros_por_autor_id:
        print(f"ID do Livro: {livro.livro_id_livro}")


    # Consulta 10: Buscar livros por editora ID
    livros_por_editora_id = Livro_editora.buscar_por_editora_id(3)
    print("\nLivros encontrados pelo ID da editora 3:")
    for livro in livros_por_editora_id:
        print(f"ID do Livro: {livro.livro_id_livro}")

    # Consulta 11: Buscar vendas por quantidade
    vendas_por_quantidade = Livro_venda.buscar_por_quantidade(2)
    print("\nVendas encontradas com quantidade 2:")
    for venda in vendas_por_quantidade:
        print(f"ID da Venda: {venda.venda_id_venda}")

    # Consulta 12: Buscar autores pelo nome
    autores_por_nome = Autores.buscar_por_nome("Autor 1", session)
    print("Autores encontrados pelo nome 'Autor 1':")
    for autor in autores_por_nome:
        print(f"ID: {autor.id_autores}, Nome: {autor.nome}")

    # Consulta 13: Buscar livro pelo ID
    livro_por_id = Livro.buscar_por_id(2, session)
    print("\nLivro encontrado pelo ID 2:")
    if livro_por_id:
        print(f"ID: {livro_por_id.id_livro}, Nome: {livro_por_id.nome}")

    # Consulta 14: Buscar método de pagamento pelo tipo
    metodo_pagamento_por_tipo = Metodo_pagamento.buscar_por_tipo("Crédito", session)
    print("\nMétodo de pagamento encontrado pelo tipo 'Crédito':")
    for metodo in metodo_pagamento_por_tipo:
        print(f"ID: {metodo.id_metodo_pagamento}, Tipo: {metodo.tipo}")

    # Consulta 15: Buscar cliente pelo email
    cliente_por_email = Cliente.buscar_por_email("cliente3@example.com", session)
    print("\nCliente encontrado pelo email 'cliente3@example.com':")
    for cliente in cliente_por_email:
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}")

    # Consulta 16: Buscar avaliação por estrelas
    avaliacao_por_estrelas = Avaliacao.buscar_por_estrelas(5, session)
    print("\nAvaliações com 5 estrelas:")
    for avaliacao in avaliacao_por_estrelas:
        print(f"ID: {avaliacao.id_avaliacao}, Estrelas: {avaliacao.estrelas}")

    # Consulta 17: Buscar categoria pelo nome
    categoria_por_nome = Categoria.buscar_por_nome("Ficção", session)
    print("\nCategorias com o nome 'Ficção':")
    for categoria in categoria_por_nome:
        print(f"ID: {categoria.id_categoria}, Nome: {categoria.nome}")

    # Consulta 18: Buscar editora por exemplares vendidos
    editora_por_exemplares = Editora.buscar_por_exemplares_vendidos(1000, session)
    print("\nEditoras com 1000 exemplares vendidos:")
    for editora in editora_por_exemplares:
        print(f"ID: {editora.id_editora}, Nome: {editora.nome}")

    # Consulta 19: Buscar venda por data
    venda_por_data = Venda.buscar_por_data(date(2023, 5, 1), session)
    print("\nVendas na data '2023-05-01':")
    for venda in venda_por_data:
        print(f"ID: {venda.id_venda}, Data: {venda.data}")

    # Consulta 20: Buscar Livro_autores por autor_id
    livro_autores_por_autor_id = Livro_autores.buscar_por_autor_id(1, session)
    print("\nLivros do autor com ID 1:")
    for livro_autor in livro_autores_por_autor_id:
        print(f"Autor ID: {livro_autor.autor_id_autores}, Livro ID: {livro_autor.livro_id_livro}")

consultar_dados()