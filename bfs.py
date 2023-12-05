from collections import deque

def bfs(grafo, nodoInicial):
    # Inicia una cola para hacer la busqueda (FIFO)
    cola = deque([nodoInicial])
    
    # Inicia un conjunto para hacer un registro de los nodos visitados
    visitados = set([nodoInicial])

    print(nodoInicial, end=' ')

    while cola:
        nodoActual = cola.popleft()  # obtener y eliminar el primer nodo de la cola
        for vecinos_diccionario in grafo.grafo[nodoActual]:
            vecino = list(vecinos_diccionario.keys())[0] # obtiene el vecino del diccionario
            if vecino not in visitados:
                print(vecino, end=' ')
                visitados.add(vecino)
                cola.append(vecino)
