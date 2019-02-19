import numpy as np
# Matrix limitations
# 
# number on the diagonal >= sum of two other numbers (!)
# there shouldn't be division by 0
#    [b1 c1 0  0 ... 0]
#    [a1 b2 c2 0 ... 0]
# A =[0 a2 b3 c3 ... 0]
#    [ .............. ]
#    [0 0... a(n-1) bn]

def solve(a, b, c, d):
	# Solve A*x=d
	
	alpha = [c[0]/b[0]]
	beta = [d[0]/b[0]]
	
	# iteratively count alpha and beta, because they depend on their previous iteration
	for i in range(1,len(b)):
		if i != len(b)-1:
			alpha.append(c[i]/(b[i]-alpha[-1]*a[i-1]))
		beta.append((d[i]-beta[-1]*a[i-1])/(b[i]-alpha[-1]*a[i-1]))
		
	x = [0 for x in range(len(b))]
	x[-1] = beta[-1]
	
	# reversed iteration to find x with some small error due to many repetitions
	for i in reversed(range(len(b)-1)):
		x[i] = beta[i]-alpha[i]*x[i+1]
		
	return x

a = [1 for x in range(999)] # lower diagonal
b = [-4 for x in range(1000)] # diagonal
c = [1 for x in range(999)] # upper diagonal
d = [-6] 
for i in range(998):
	d.append(-4)
d.append(-6)

print(solve(a,b,c,d))
