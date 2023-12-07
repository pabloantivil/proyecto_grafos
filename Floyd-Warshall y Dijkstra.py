class Graph():
    def __init__(self):
        self.grafo = dict()

    def add_V(self, v):
        if v in self.grafo:
            print("Vertice existente")
        else:
            self.grafo.update({v: []})

    def add_E(self, v1, v2, peso):
        if v1 in self.grafo and v2 in self.grafo:
            if self.grafo[v1]:
                a = True
                for x in range(len(self.grafo[v1])):
                    if v2 not in list(self.grafo[v1][x].keys()):
                        a = True
                    else:
                        a = False
                        print("Conexion existente")
                        break
                if a == True:
                    print(self.grafo[v1][x].keys(), v2)
                    self.grafo[v1].append({v2: peso})
            else:
                self.grafo[v1].append({v2: peso})
        else:
            print("No vertice")

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
        print(vecino_menor)
        return vecino_menor

    def dikjstra(self, salida):
        dist = {v: float('inf') for v in self.grafo}
        prev = {v: None for v in self.grafo}
        dist[salida] = 0

        Q = [v for v in self.grafo]

        while Q:
            u = self.minimo([{v: dist[v]} for v in Q])
            Q.remove(u)

            for x in self.grafo[u]:
                vecino, peso = list(x.items())[0]
                if dist[vecino] > dist[u] + peso:
                    dist[vecino] = dist[u] + peso
                    prev[vecino] = u

        return dist, prev


g = Graph()
g.add_V(1)
g.add_V(2)
g.add_V(3)
g.add_V(4)

g.add_E(1, 2, 1)
g.add_E(2, 1, 1)
g.add_E(3, 4, 20)

print(g.grafo)

print("Floyd-Warshall:", g.floyd_warshall())
print("Dikjstra", g.dikjstra(1))
