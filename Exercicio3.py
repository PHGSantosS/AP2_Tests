def validar_documento(documento):
    if documento is None:
        return False

    documento_limpo = str(documento).replace('.', '').replace('-', '').replace(' ', '')
    return documento_limpo.isdigit() and len(documento_limpo) == 11
