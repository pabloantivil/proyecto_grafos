def prim(grafo, inicio):
    visitados = set()
    aristas = []

    for v1 in grafo.grafo:
        for conexion in grafo.grafo[v1]:
            v2 = list(conexion.keys())[0]
            peso = conexion[v2]
            aristas.append([v1, v2, peso])

    aristas_ordenadas = sorted(aristas, key=lambda item: item[2])
    aristas_arbol_minimo = []

    visitados.add(inicio)

    for arista in aristas_ordenadas:
        v1, v2, peso = arista

        # Considerar solo aristas dirigidas hacia vértices no visitados
        if v1 in visitados and v2 not in visitados:
            visitados.add(v2)
            aristas_arbol_minimo.append([v1, v2, peso])

    print(aristas_arbol_minimo)
    return aristas_arbol_minimo
