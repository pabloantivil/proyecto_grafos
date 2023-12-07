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