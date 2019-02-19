import numpy as np
import math

func = lambda x: x + math.sin(x) - 1
	
a = 0
b = math.pi/2
eps = 10e-4
i=0

while abs(a-b)>eps:

	if np.sign(func(a))==np.sign(func((a+b)/2)):
		a = (a+b)/2
		
	else:
		b = (a+b)/2
	i+=1	
	print("Itaration {} : {}, {}".format(i,a,b))