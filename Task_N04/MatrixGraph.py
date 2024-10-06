from __future__ import annotations
import random

class ListGraph:
    def __init__(self, V) -> None:
        self.V = V
        self.L = [[] for i in range(self.V)]

    
    def add_vert(self) -> None:
        self.L.append([])
        self.V += 1
    

    def del_vert(self, vert) -> None:
        self.L.pop(vert)
        for u in self.L:
            u.remove(vert)
        self.V -= 1


    def del_edge(self, u, v):
        if u <= self.V:
            for vw in self.L[u]:
                if vw[0] == v:
                    self.L[u].remove(vw)


    def add_edge(self, u, v, w) -> None:
        self.del_edge(u, v)
        self.L[u].append((v, w))


    def list2matrix(self) -> OrientedWeightedMatrixGraph:
        Matrix = OrientedWeightedMatrixGraph(self.V)
        for u in range(self.V):
            for vw in self.L[u]:
                Matrix[u][vw[0]] = vw[1]
        return Matrix
    

    def __str__(self) -> str:
        res = ""
        for i in range(self.V):
            res += f"{i} : {self.L[i]} \n"
        return res
    

class OrientedWeightedMatrixGraph:
    def __init__(self, V) -> None:
        self.V = V
        self.matrix = [[float('inf')]*self.V for i in range(V)]


    def add_vert(self) -> None:
        for i in range(self.V):
            self.matrix[i].append(float('inf'))
        self.matrix.append([float('inf')]*self.V)
        self.V += 1


    def del_vert(self, vert: int) -> None:
        self.matrix.pop(vert)
        for i in range(self.V-1):
            self.matrix[i].pop(vert)
        self.V -= 1
    

    def add_edge(self, u, v, w) -> None:
        self.matrix[u][v] = w
    

    def del_edge(self, u, v) -> None:
        self.matrix[u][v] = float('inf')
    

    def matrix2list(self) -> list:
        List = ListGraph(self.V)
        for i in range(self.V):
            for j in range(self.V):
                w = self.matrix[i][j]
                if w is not float('inf'):
                    List.add_edge(i, j, w)
        return List
    

    def model_Erdasha_Renya(self, p: float, 
                            w_min: float = -10, 
                            w_max: float = 10):
        for i in range(self.V):
            for j in range(self.V):
                if random.random() <= p and i!=j:
                    self.add_edge(i, j, random.random()*abs(w_max - w_min) + w_min)

    

    def __str__(self) -> str:
        res = "["
        for a in self.matrix:
            res += str(a) + "\n "
        res = res[:-2:] + str("]\n")
        return res
    

class NonOrientedWeightedMatrixGraph(OrientedWeightedMatrixGraph):
    def add_edge(self, u, v, w) -> None:
        super().add_edge(u, v, w)
        super().add_edge(v, u, w)
    

    def del_edge(self, u, v) -> None:
        super().del_edge(u, v)
        super().del_edge(v, u)


class OrientedMatrixGraph(OrientedWeightedMatrixGraph):
    def add_edge(self, u, v) -> None:
        return super().add_edge(u, v, 1)
    

    def model_Erdasha_Renya(self, p: float):
        for i in range(self.V):
            for j in range(self.V):
                if random.random() <= p and i!=j:
                    self.add_edge(i, j)
    

class NonOrientedMatrixGraph(NonOrientedWeightedMatrixGraph):
    def add_edge(self, u, v) -> None:
        return super().add_edge(u, v, 1)
    

    def model_Erdasha_Renya(self, p: float):
        for i in range(self.V):
            for j in range(self.V):
                if random.random() <= p and i!=j:
                    self.add_edge(i, j)