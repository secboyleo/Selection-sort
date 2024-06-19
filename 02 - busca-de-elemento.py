def busca(lista, elemento):
    tam = len(lista)
    x = 0
    for i in range(tam):
        if lista[i] == elemento:
            return i
            break
    return False