from Exercicio3 import validar_documento


def test_documento_valido():
    assert validar_documento("12345678900") is True

def test_documento_formatado():
    assert validar_documento("123.456.789-00") is True

def test_documento_com_valor_menor_que_11():
    assert validar_documento("1234567890") is False

def test_documento_com_valor_maior_que_11():
    assert validar_documento("123456789000") is False

def test_documento_com_caracteres_invalidos():
    assert validar_documento("123.456.789-0A") is False

def test_documento_nulo():
    assert validar_documento("") is False
