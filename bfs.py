from collections import deque


def bfs(grafo, nodoInicial):
    # Inicia una cola para hacer la busqueda (FIFO)
    cola = deque([nodoInicial])

    # Inicia un conjunto para hacer un registro de los nodos visitados
    visitados = set([nodoInicial])

    print(nodoInicial, end=':0 ')
    c = 1
    while cola:
        nodoActual = cola.popleft()  # obtener y eliminar el primer nodo de la cola
        for vecinos_diccionario in grafo.grafo[nodoActual]:
            # obtiene el vecino del diccionario
            vecino = list(vecinos_diccionario.keys())[0]
            if vecino not in visitados:
                print(vecino, end=f':{c} ')
                visitados.add(vecino)
                cola.append(vecino)
        c += 1
