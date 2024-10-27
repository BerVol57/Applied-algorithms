from matrix import *
import unittest


a = [[1, 2, 1], 
     [2, 1, 2], 
     [1, 2, 1]]

b = [[2, 1, 2], 
     [1, 2, 1], 
     [2, 1, 2]]

ma = matrix(a)
mb = matrix(b)

c = [1, 2, 3]
d = [4, 5, 6]

vc = vector(c)
vd = vector(d)


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(str(ma + mb), str(matrix([[3, 3, 3], 
                                                   [3, 3, 3], 
                                                   [3, 3, 3]])))
        self.assertEqual(str(vc + vd), str(vector([5, 7, 9])))
        
    def test_sub(self):
        self.assertEqual(str(ma - mb), str(matrix([[-1,  1, -1], 
                                                   [ 1, -1,  1], 
                                                   [-1,  1, -1]])))
        self.assertEqual(str(vc - vd), str(vector([-3, -3, -3])))

    def test_mul(self):
        self.assertEqual(str(ma * mb), str(matrix([[6, 6, 6], 
                                                   [9, 6, 9], 
                                                   [6, 6, 6]])))
        self.assertEqual(str(ma * vc), str(vector([8, 10, 8])))
        self.assertEqual(vc * vd, 32)

if __name__ == '__main__':
    unittest.main()