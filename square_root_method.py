import numpy as np
import scipy.linalg

def solveS(A):
	L, U = scipy.linalg.lu(A,permute_l=True)
	U /= np.floor(np.sqrt(np.diag(A)))[:,None]
	return U
	
def solveX(S,b):
	y = np.linalg.solve(S.T,b)
	return np.linalg.solve(S,y)
	
A = np.array([[36,-18,3],[-18,34,-11.5],[3,-11.5,20.25]])
b = np.array([21,4.5,11.75])

S = solveS(A)

print("Answer: \n",solveX(S,b))