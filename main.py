from grafo import Graph
from dfs import dfs
from bfs import bfs
from kruskal import kruskal
from graficar import visualizar_grafo
from lol import floyd_warshall, minimo, dijkstra

# Crear una instancia de la clase Graph
grafo = Graph()

# Agregar vertices y aristas al grafo
grafo.add_V('A')
grafo.add_V('B')
grafo.add_V('C')
grafo.add_V('D')
grafo.add_V('E')
grafo.add_E('A', 'B', 1)
grafo.add_E('B', 'C', 2)
grafo.add_E('A', 'D', 1)
grafo.add_E('B', 'E', 1)


Graph.floyd_warshall = floyd_warshall
print(grafo.floyd_warshall())
Graph.minimo = minimo
Graph.dijkstra = dijkstra
print(grafo.dijkstra('A'))

# Algoritmo DFS
# print("DFS:")
# dfs(grafo, 'A')

# Algoritmo BFS
# print("BFS:")
# bfs(grafo, 'A')

# gr = kruskal(grafo)
# visualizar_grafo(grafo , gr , titulo="Grafo Kruskal")
