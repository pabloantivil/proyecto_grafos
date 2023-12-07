from grafo import Graph
from dfs import dfs
from bfs import bfs
from kruskal import kruskal
from graficar import visualizar_grafo
from prim import prim
from lol import floyd_warshall, minimo, dijkstra
from emparejamiento import emparejamiento

# Crear una instancia de la clase Graph
grafo = Graph()
grafo_emparejamiento = Graph()

# Agregar vertices y aristas al grafo
grafo.add_V('A')
grafo.add_V('B')
grafo.add_V('C')
grafo.add_V('D')
grafo.add_V('E')
grafo.add_E('A', 'B', 1)
grafo.add_E('A', 'E', 2)
grafo.add_E('B', 'C', 2)
grafo.add_E('A', 'D', 1)
grafo.add_E('B', 'E', 1)

# Emparejamiento
grafo_emparejamiento.add_V_pref("M1", ["W3", "W2", "W1"])
grafo_emparejamiento.add_V_pref("M2", ["W3", "W2", "W1"])
grafo_emparejamiento.add_V_pref("M3", ["W3", "W1", "W2"])

grafo_emparejamiento.add_V_pref("W1", ["M2", "M1", "M3"])
grafo_emparejamiento.add_V_pref("W2", ["M3", "M2", "M3"])
grafo_emparejamiento.add_V_pref("W3", ["M1", "M3", "M2"])

Graph.emparejamiento = emparejamiento
print('Emparejamiento: ')
grafo_emparejamiento.emparejamiento()

# Algoritmo BFS
print("BFS:")
bfs(grafo, 'A')


# Algoritmo DFS
print("\nDFS:")
dfs(grafo, 'A')

# Dijkstra
Graph.minimo = minimo
Graph.dijkstra = dijkstra
print('\nDijkstra: \n', grafo.dijkstra('A'))

# Floyd-Warshall
Graph.floyd_warshall = floyd_warshall
print('\nfloyd_warshall: \n', grafo.floyd_warshall())


# Algoritmo Kruskal
gr = kruskal(grafo)
visualizar_grafo(grafo, gr, titulo="Grafo Kruskal")


# Aplicar el algoritmo de Prim con un nodo de inicio
nodo_inicio = 'A'
arbol_minimo_prim = prim(grafo, nodo_inicio)

# Visualizar el grafo original con las aristas del árbol mínimo en rojo
visualizar_grafo(grafo, arbol_minimo_prim,
                 "Grafo Original con Árbol Mínimo (Prim)")

