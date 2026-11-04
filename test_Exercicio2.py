from Exercicio2 import inverter_palavras


def test_inverter_palavras():
    assert inverter_palavras("Python é muito interessante") == "interessante muito é Python"

def test_inverter_palavras_com_uma_palavra():
    assert inverter_palavras("Python") == "Python"

def test_inverter_palavras_frase_vazia ():
    assert inverter_palavras("") == ""

def test_inverter_palavras_com_espacos_extras():
    assert inverter_palavras("  Python   é   muito   interessante  ") == "interessante muito é Python"

def test_inverter_palavras_com_numeros_e_letras():
    assert inverter_palavras("123 abc 456 def") == "def 456 abc 123"
