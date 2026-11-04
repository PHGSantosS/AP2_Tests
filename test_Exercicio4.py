from unittest.mock import patch

from Exercicio4 import criar_identificacao, gerar_codigo


def test_verificar_mensagem_gerada_corretamente():
    with patch("Exercicio4.gerar_codigo", return_value="USR-1234"):
        mensagem = criar_identificacao("Carlos")

    assert mensagem == "Usuário Carlos cadastrado com código USR-1234."


def test_verificar_gerar_codigo_foi_chamada():
    with patch("Exercicio4.gerar_codigo", return_value="USR-1234") as mock_gerar_codigo:
        criar_identificacao("Carlos")

    mock_gerar_codigo.assert_called_once()


def test_verificar_funcao_chamada_uma_unica_vez():
    with patch("Exercicio4.gerar_codigo", return_value="USR-5678") as mock_gerar_codigo:
        criar_identificacao("Ana")

    assert mock_gerar_codigo.call_count == 1


def test_utilizar_mock_para_simular_diferentes_codigos():
    with patch("Exercicio4.gerar_codigo", side_effect=["USR-1000", "USR-2000"]):
        primeira = criar_identificacao("Carlos")
        segunda = criar_identificacao("Maria")

    assert primeira == "Usuário Carlos cadastrado com código USR-1000."
    assert segunda == "Usuário Maria cadastrado com código USR-2000."


def test_comportamento_com_nomes_diferentes():
    with patch("Exercicio4.gerar_codigo", return_value="USR-9999"):
        mensagem1 = criar_identificacao("Carlos")
        mensagem2 = criar_identificacao("Beatriz")

    assert mensagem1 == "Usuário Carlos cadastrado com código USR-9999."
    assert mensagem2 == "Usuário Beatriz cadastrado com código USR-9999."
