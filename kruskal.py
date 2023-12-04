def kruskal(grafo):
    aristas = []

    for v1 in grafo.grafo:
        for conexion in grafo.grafo[v1]:
            v2 = list(conexion.keys())[0]
            peso = conexion[v2]
            aristas.append([v1, v2, peso])

    aristas_ordenadas = sorted(aristas, key=lambda item: item[2])
    resultado = []
    subconjuntos = {v: {v} for v in grafo.grafo}

    for arista in aristas_ordenadas:
        v1, v2, peso = arista
        conjunto_v1 = subconjuntos[v1]
        conjunto_v2 = subconjuntos[v2]

        if conjunto_v1 != conjunto_v2:
            resultado.append([v1, v2, peso])
            nuevo_conjunto = conjunto_v1.union(conjunto_v2)

            for vertice in nuevo_conjunto:
                subconjuntos[vertice] = nuevo_conjunto
    print(resultado)
    return resultado