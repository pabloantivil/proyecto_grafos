from grafo import Graph
from dfs import dfs

# Crear una instancia de la clase Graph
grafo = Graph()

# Agregar vertices y aristas a tu grafo
grafo.add_V('A')
grafo.add_V('B')
grafo.add_V('C')
grafo.add_E('A', 'B', 1)
grafo.add_E('B', 'C', 2)


# Algoritmo DFS
print("DFS:")
dfs(grafo, 'A')
