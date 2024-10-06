class UnionFind:
    def __init__(self, n: int) -> None:
        self.R = {i: i for i in range(n)}
        self.List = {i: i for i in range(n)}
        self.Next = {i: None for i in range(n)}
        self.Size = {i: 1 for i in range(n)}

        self.InternalNames = {i: i for i in range(n)}
        self.ExternalNames = {i: i for i in range(n)}


    def MakeSet(self) -> None:
        len_R = len(self.R)
        self.R[len_R] = len_R
        self.List[len_R] = len_R
        self.Next[len_R] = None
        self.Size[len_R] = 1

        self.InternalNames[len_R+1] = len_R
        self.ExternalNames[len_R] = len_R+1

    
    def Find(self, x):
        return self.ExternalNames[self.R[x]]
    
    def FindInt(self, x):
        return self.InternalNames[self.R[x]]

    def Union(self, x, y) -> None:
        A, B = self.R[x], self.R[y]
        if self.Size[A] > self.Size[B]:
            A, B = B, A
        z = self.List[A]
        while z is not None:
            
            self.R[z] = B
            last = z
            z = self.Next[z]

        self.Next[last] = self.List[B]
        self.List[B] = self.List.pop(A)
        # self.List.pop(A)
        self.Size[B] += self.Size.pop(A)
        # self.Size.pop(A)
        self.InternalNames[x] = B
        self.ExternalNames[B] = x


    def show(self) -> None:
        print(f"R:{self.R}")
        print(f"List:{self.List}")
        print(f"Next:{self.Next}")
        print(f"Size:{self.Size}")
        print(f"Internal:{self.InternalNames}")
        print(f"External:{self.ExternalNames}")