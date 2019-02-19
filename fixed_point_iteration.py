import math

func = lambda x: math.sqrt(x+9) + 1
	
i=0
x = 0
x1 = func(x)
eps = 10e-5
while abs(x-x1)>eps:
	if i > 0:
		x = x1
		x1 = func(x)
	print(i,x)
	i+=1