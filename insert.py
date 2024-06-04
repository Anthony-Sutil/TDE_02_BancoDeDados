from sqlalchemy.orm import Session
from datetime import date
from app import Autores, Livro, Metodo_pagamento, Cliente, Avaliacao, Categoria, Editora, Venda, Livro_autores, Livro_categoria, Livro_editora, Livro_venda
from connection import engine

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
