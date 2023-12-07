def floyd_warshall(self):
    vertices = list(self.grafo.keys())
    distance_matrix = {v1: {v2: float('infinity')
                            for v2 in vertices} for v1 in vertices}

    for v1 in self.grafo:
        for x in self.grafo[v1]:
            v2, peso = list(x.items())[0]
            distance_matrix[v1][v2] = peso

    for v in vertices:
        distance_matrix[v][v] = 0

    for k in vertices:
        for i in vertices:
            for j in vertices:
                distance_matrix[i][j] = min(
                    distance_matrix[i][j],
                    distance_matrix[i][k] + distance_matrix[k][j]
                )
    return distance_matrix


def minimo(self, lista):
    menor = list(lista[0].values())[0]
    vecino_menor = list(lista[0].keys())[0]
    for x in lista:
        key, value = list(x.items())[0]
        if value < menor:
            menor = value
            vecino_menor = key
    return vecino_menor


def dijkstra(self, salida):
    dist = {v: float('inf') for v in self.grafo}
    prev = {v: None for v in self.grafo}
    dist[salida] = 0

    Q = [v for v in self.grafo]

    while Q:
        u = self.minimo([{v: dist[v]} for v in Q])
        Q.remove(u)

        for x in self.grafo[u]:
            vecino, peso = list(x.items())[0]
            # Relajar arista
            if dist[vecino] > dist[u] + peso:
                dist[vecino] = dist[u] + peso
                prev[vecino] = u

    return dist, prev
