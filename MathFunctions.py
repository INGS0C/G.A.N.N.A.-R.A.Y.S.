from random import randrange
from math import e as E

class Matrix:
    main_list = []


    def __init__( self, rows=1, columns=1 ):
        self.main_list = [[0 for _ in range(columns)] for _ in range(rows)]


    def assign( self, value, r=0, c=0 ):
        self.main_list[r][c] = value


    def totalAssign(self, matrix_list):
        self.main_list = [[0 for _ in range(len(matrix_list[0]))] for _ in range(len(matrix_list))]
        for r in range(len(self.main_list)):
            for c in range(len(self.main_list[0])):
                self.main_list[r][c] = matrix_list[r][c]


    def returnFunc(self, rows, columns):
        return [[self.main_list[r][c] for c in columns] for r in rows]


    def read(self, rows=None, columns=None):
        if rows==None and columns==None:
            return self.returnFunc(
                [x for x in range(len(self.main_list))],
                [x for x in range(len(self.main_list[0]))]
            )
        else:
            pass_rows = rows
            pass_columns = columns
            if pass_rows==None: pass_rows = [x for x in range(len(self.main_list))]
            if pass_columns==None: pass_columns = [x for x in range(len(self.main_list[0]))]
            return self.returnFunc(pass_rows, pass_columns)


    def fill(self, value):
        for r in range(len(self.main_list)):
            for c in range(len(self.main_list[0])):
                self.main_list[r][c] = value


    def addRow(self, index=0, list=None):
        if list == None:
            self.main_list.insert(index, [0 for _ in range(len(self.main_list[0]))])


    def addColumn(self, index=0, list=None):
        for r in range(len(self.main_list)):
            self.main_list[r].insert(index, 0)


    def randomize(self, start, end, decimal=1):
        for r in range(len(self.main_list)):
            for c in range(len(self.main_list[0])):
                self.main_list[r][c] = randrange(start*decimal, end*decimal)/decimal


    def scale(self, scalar):
        for r in range(len(self.main_list)):
            for c in range(len(self.main_list[0])):
                self.main_list[r][c] *= scalar


def matrixMult(matrix_one, matrix_two):
    return_matrix = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(matrix_one))]
    for r in range(len(matrix_one)):
        for c in range(len(matrix_two[0])):
            for i in range(len(matrix_two)):
                return_matrix[r][c] += matrix_one[r][i] * matrix_two[i][c]
    return return_matrix

def sigma(value):
    return 1/(1+E**(-value))

if __name__ == '__main__':
    pass