import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(g, resultado_kruskal , titulo="hola"):
    plt.close()
    G = nx.Graph()

    for v1 in g.grafo:
        G.add_node(v1)

        for conexion in g.grafo[v1]:
            v2 = list(conexion.keys())[0]
            peso = conexion[v2]
            G.add_edge(v1, v2, weight=peso)

    pos = nx.spring_layout(G)  # Puedes cambiar el diseño aquí según tus preferencias

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue", font_color="black")

    # Resaltar aristas del árbol de expansión mínima en rojo
    aristas_kruskal = [(str(v1), str(v2)) for v1, v2, peso in resultado_kruskal]
    edgelist_kruskal = [edge for edge in G.edges if edge in aristas_kruskal]
    nx.draw_networkx_edges(G, pos, edgelist=edgelist_kruskal, edge_color="red", width=2)

    # Mostrar pesos de las aristas
    edge_labels = {(str(v1), str(v2)): peso for v1, v2, peso in resultado_kruskal}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.get_current_fig_manager().set_window_title(titulo)
    plt.show()