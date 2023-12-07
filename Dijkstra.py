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
               

    return dist
