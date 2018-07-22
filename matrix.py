import random

from copy import deepcopy

class Matrix():

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.nrows=nrows 
        self.ncols=ncols
        for i in range(int(self.nrows)):
            for j in range(int(self.ncols)):
                print(random.randint(0,9),end=' ') 
            print("")

    def add(self, m):
        """return a new Matrix object after summation"""
        print("========== A + B ==========")
    def sub(self, m):
        """return a new Matrix object after substraction"""
        print("========== A - B ==========")

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        print("========== A * B ==========")

    def transpose(self):
        """return a new Matrix object after transpose"""
        #print (list(map(list, zip(*self.matrix))))
    
    def display(self):
        """Display the content in the matrix"""
        pass

nrows=Matrix(input("Enter A Matrix's rows:"),input("Enter A Matrix's cols:"))
ncols=Matrix(input("Enter B Matrix's rows:"),input("Enter B Matrix's cols:"))
