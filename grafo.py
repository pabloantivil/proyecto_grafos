class Graph():
    def __init__(self):
        self.grafo = dict()

    def add_V(self, v):
        if v in self.grafo:
            print("Vertice existente")
        else:
            self.grafo.update({v: []})

    def add_E(self, v1, v2, peso):
        if v1 in self.grafo and v2 in self.grafo:
            if self.grafo[v1]:
                a = True
                for x in range(len(self.grafo[v1])):
                    if v2 not in list(self.grafo[v1][x].keys()):
                        a = True
                    else:
                        a = False
                        print("Conexion existente")
                        break
                if a == True:
                    self.grafo[v1].append({v2: peso})
            else:
                self.grafo[v1].append({v2: peso})
        else:
            print("No vertice")

    def add_V_pref(self, v, pref):
        if v in self.grafo:
            print("Vertice existente")
        else:
            self.grafo.update({v: pref})
