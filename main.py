from grafo import Graph ; from dfs import dfs ; from bfs import bfs; from kruskal import kruskal 
from graficar import visualizar_grafo ;

# Crear una instancia de la clase Graph
grafo = Graph()

# Agregar vertices y aristas al grafo
grafo.add_V('A')
grafo.add_V('B')
grafo.add_V('C')
<<<<<<< HEAD
grafo.add_V('O')


grafo.add_E('A', 'B', 1)
grafo.add_E('B', 'C', 2)
grafo.add_E('A' , 'C' , 1)
grafo.add_E('A' , 'O' , 7)
grafo.add_E('B' , 'O' , 1)

=======
grafo.add_V('D')
grafo.add_V('E')
grafo.add_E('A', 'B', 1)
grafo.add_E('B', 'C', 2)
grafo.add_E('A' , 'D' , 1)
grafo.add_E('B' , 'E' , 1)
>>>>>>> 3de31090fa357621974a6681603ed7b488fdc059

# Algoritmo DFS
# print("DFS:")
# dfs(grafo, 'A')

# Algoritmo BFS
# print("BFS:")
# bfs(grafo, 'A')

# gr = kruskal(grafo)
# visualizar_grafo(grafo , gr , titulo="Grafo Kruskal")

