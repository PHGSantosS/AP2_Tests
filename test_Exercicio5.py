from unittest.mock import patch

from Exercicio5 import acessar_sistema, verificar_permissao


def test_usuario_com_permissao():
    assert verificar_permissao("admin") is True


def test_usuario_sem_permissao():
    assert verificar_permissao("visitante") is False


def test_verificar_permissao_foi_chamada():
    with patch("Exercicio5.verificar_permissao", return_value=True) as mock_permissao:
        acessar_sistema("admin")

    mock_permissao.assert_called_once_with("admin")


def test_verificar_se_foi_chamada_com_o_usuario_correto():
    with patch("Exercicio5.verificar_permissao", return_value=False) as mock_permissao:
        acessar_sistema("visitante")

    mock_permissao.assert_called_once_with("visitante")


def test_utilizar_mock_para_simular_dois_cenarios():
    with patch("Exercicio5.verificar_permissao", side_effect=[True, False]):
        assert acessar_sistema("admin") == "Acesso autorizado"
        assert acessar_sistema("visitante") == "Acesso negado"
