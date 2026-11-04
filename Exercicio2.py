def inverter_palavras(texto):
    if not texto:
        return ""

    palavras = texto.split()
    return ' '.join(reversed(palavras))