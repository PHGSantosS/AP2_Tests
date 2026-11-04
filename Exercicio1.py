def classificar_produto(quantidade):
    if quantidade == 0:
        return "Sem Estoque"
    elif 1 <= quantidade <= 5:
        return "Estoque Baixo"
    elif 6 <= quantidade <= 20:
        return "Estoquee Normal"
    elif quantidade > 20:
        return "Estoqueee Alto"
    else:
        return "Quantidade inválida"