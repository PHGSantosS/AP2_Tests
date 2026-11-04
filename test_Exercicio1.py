from Exercicio1 import classificar_produto

def test_classificar_produto():
    assert classificar_produto(0) == "Sem Estoque"

def test_classificar_produto_baixo_estoque():
    assert classificar_produto(3) == "Estoque Baixo"

def test_classificar_produto_estoque_normal():
    assert classificar_produto(10) == "Estoque Normal"

def test_classificar_produto_estoque_alto():
    assert classificar_produto(25) == "Estoque Alto"

def test_classificar_produto_quantidade_invalida():
    assert classificar_produto(-1) == "Quantidade inválida"