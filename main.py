from grafo import Graph ; from dfs import dfs ; from kruskal import kruskal 
from graficar import visualizar_grafo ;

# Crear una instancia de la clase Graph
grafo = Graph()

# Agregar vertices y aristas a tu grafo
grafo.add_V('A')
grafo.add_V('B')
grafo.add_V('C')
grafo.add_E('A', 'B', 1)
grafo.add_E('B', 'C', 2)
grafo.add_E('A' , 'C' , 1)



# Algoritmo DFS
print("DFS:")
dfs(grafo, 'A')
gr = kruskal(grafo)

visualizar_grafo(grafo , gr , titulo="Grafo Kruskal")

