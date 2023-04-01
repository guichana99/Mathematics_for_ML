#This code is for solving simultaneous equations with vectors
#Using numpy
#My equation is 2a + 3b = 10 and 10a + 9b = 32

import numpy as np

#Define the coefficients of the equations
A = np.array([[2,3],[10,9]])
B = np.array([10,32])

#Solving equation
#Used np.linalg.solve(See numpy official doc for more)
X = np.linalg.solve(A,B)

#Print solution
print(f"The solution is x = {X[0]},y = {X[1]}")
