from grafo import Graph ; from dfs import dfs ; from bfs import bfs; from kruskal import kruskal 
from graficar import visualizar_grafo ; from prim import prim

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
grafo.add_E('A' , 'D' , 1)
grafo.add_E('B' , 'E' , 1)

print(grafo.grafo)
# Algoritmo DFS
# print("DFS:")
# dfs(grafo, 'A')

# Algoritmo BFS
# print("BFS:")
# bfs(grafo, 'A')

#gr = kruskal(grafo)
#visualizar_grafo(grafo , gr , titulo="Grafo Kruskal")

# Aplicar el algoritmo de Prim con un nodo de inicio
#nodo_inicio = 'A'
#arbol_minimo_prim = prim(grafo, nodo_inicio)

# Visualizar el grafo original con las aristas del árbol mínimo en rojo
#visualizar_grafo(grafo, arbol_minimo_prim, "Grafo Original con Árbol Mínimo (Prim)")
#print(arbol_minimo_prim)


