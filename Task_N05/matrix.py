from __future__ import annotations

class matrix:
    def __init__(self, mlist: list) -> None:
        self.mlist = mlist
        self.length = len(mlist)
        
        for a in mlist:
            if len(a) != self.length:
                raise ValueError("Not square matrix")
    
    
    def __str__(self) -> str:
        res = ""
        for l in self.mlist:
            res += str(l)+"\n"
        return res[:-1]
    
    
    # def add
    def __add__(self, other: matrix) -> matrix:
        res = []
        for i in range(self.length):
            res.append([])
            for j in range(self.length):
                res[-1].append(self.mlist[i][j]+other.mlist[i][j])
        return matrix(res)
    
    
    # def sub
    def __sub__(self, other: matrix) -> matrix:
        res = []
        for i in range(self.length):
            res.append([])
            for j in range(self.length):
                res[-1].append(self.mlist[i][j]-other.mlist[i][j])
        return matrix(res)
    
    
    # def mul matrix
    def __mul__(self, other) -> matrix:
        res = []
        if type(other) == matrix:
            for i in range(self.length):
                res.append([])
                for j in range(self.length):
                    temp = 0
                    for k in range(self.length):
                        temp += self.mlist[i][k] * other.mlist[k][j]
                    res[-1].append(temp)
            return matrix(res)
        elif type(other) == vector:
            if other.length != self.length:
                raise ValueError("The vector has a length different from the length of the matrix")
            for i in range(self.length):
                temp = 0
                for k in range(self.length):
                    temp += self.mlist[i][k] * other.vec[k]
                res.append(temp)
            return vector(res)
        else:
            raise TypeError("What the type?")
    
    
    def argmax(self, k):
        res = self.mlist[k][k]
        index = k
        for i in range(k, self.length):
            el = self.mlist[i][k]
            if res < el:
                res = el
                index = i
        return index
    
    
    # def LUP
    def LUP(self):
        swapp = list(range(self.length))
        for k in range(self.length):
            
            k_ = self.argmax(k)
            if self.mlist[k_][k] == 0:
                raise ValueError("Error")
            else:
                # print(self)
                self.mlist[k], self.mlist[k_] = self.mlist[k_], self.mlist[k]
                swapp[k], swapp[k_] = swapp[k_], swapp[k]
                # print(self)
                a = self.mlist[k][k]
                for i in range(k+1, self.length):
                    self.mlist[i][k] /= a
                    for j in range(k+1, self.length):
                        self.mlist[i][j] -= self.mlist[i][k]*self.mlist[k][j]
        # print(f"P:{swapp}")
        return swapp



class vector:
    def __init__(self, vec: list) -> None:
        self.vec = vec
        self.length = len(vec)
        
    
    def __str__(self) -> str:
        return str(self.vec)
    
    
    def __add__(self, other: vector) -> vector:
        res = []
        for i in range(self.length):
            res.append(self.vec[i] + other.vec[i])
        return vector(res)
    
    
    def __sub__(self, other: vector) -> vector:
        res = []
        for i in range(self.length):
            res.append(self.vec[i] - other.vec[i])
        return vector(res)
    
    
    def __mul__(self, other: vector):
        res = 0
        for i in range(self.length):
            res += self.vec[i] * other.vec[i]
        return res