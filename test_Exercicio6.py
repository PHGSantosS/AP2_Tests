from unittest.mock import patch

from Exercicio6 import atender_proximo_cliente


def test_atendimento_realizado_com_sucesso():
    with patch("Exercicio6.obter_proximo_cliente", return_value="Carlos"), patch(
        "Exercicio6.registrar_atendimento", return_value=True
    ):
        assert atender_proximo_cliente() == "Atendimento realizado"


def test_fila_vazia():
    with patch("Exercicio6.obter_proximo_cliente", return_value=None):
        assert atender_proximo_cliente() == "Fila vazia"


def test_falha_ao_registrar_atendimento():
    with patch("Exercicio6.obter_proximo_cliente", return_value="Carlos"), patch(
        "Exercicio6.registrar_atendimento", return_value=False
    ):
        assert atender_proximo_cliente() == "Falha no atendimento"


def test_verificar_se_obter_proximo_cliente_foi_chamada():
    with patch("Exercicio6.obter_proximo_cliente", return_value="Carlos") as mock_obter:
        with patch("Exercicio6.registrar_atendimento", return_value=True):
            atender_proximo_cliente()

    mock_obter.assert_called_once_with()


def test_verificar_se_registrar_atendimento_foi_chamada_com_o_cliente_correto():
    with patch("Exercicio6.obter_proximo_cliente", return_value="Ana") as mock_obter:
        with patch("Exercicio6.registrar_atendimento", return_value=True) as mock_registrar:
            atender_proximo_cliente()

    mock_obter.assert_called_once_with()
    mock_registrar.assert_called_once_with("Ana")


def test_registrar_atendimento_nao_foi_chamada_quando_fila_vazia():
    with patch("Exercicio6.obter_proximo_cliente", return_value=None) as mock_obter:
        with patch("Exercicio6.registrar_atendimento", return_value=True) as mock_registrar:
            resultado = atender_proximo_cliente()

    assert resultado == "Fila vazia"
    mock_obter.assert_called_once_with()
    mock_registrar.assert_not_called()
