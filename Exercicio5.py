def verificar_permissao(usuario):
    usuarios_com_permissao = {"admin", "maria", "joao"}
    return usuario in usuarios_com_permissao


def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"
