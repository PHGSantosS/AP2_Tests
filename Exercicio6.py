fila = ["Carlos", "Ana", "Beto"]


def obter_proximo_cliente():
    if not fila:
        return None
    return fila[0]


def registrar_atendimento(cliente):
    if cliente is None:
        return False
    return True


def atender_proximo_cliente():
    cliente = obter_proximo_cliente()

    if cliente is None:
        return "Fila vazia"

    if registrar_atendimento(cliente):
        return "Atendimento realizado"

    return "Falha no atendimento"
