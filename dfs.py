def dfs(grafo, nodoInicial, visitados=None):
    if visitados is None:
        visitados = set()  # Inicializa el conjunto visitados

    # Imprime el nodo actual y se agrega a visitados
    print(nodoInicial, end=' ')
    visitados.add(nodoInicial)

    # Explora los nodos vecinos que no han sido visitados
    for vecinos_diccionario in grafo.grafo[nodoInicial]:
        vecino = list(vecinos_diccionario.keys())[0] # obtiene el vecino del diccionario
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
