def newton(f,df,x0,eps,max_iter):
	x_n = x0
	fx_n = f(x_n)
	for i in range(max_iter):
    
		fx_n = f(x_n)
		print("Iteration: ",i,": ",x_n)
		
		if abs(fx_n) < eps:
			print('Found solution after',i,'iterations.')
			print('Solution: ',x_n)
			return x_n
            
		Dfx_n = df(x_n)

		if Dfx_n == 0:
			print('Zero derivative. No solution found.')
			return None
            
		x_n = x_n - (fx_n/Dfx_n)

	print('Exceeded maximum iterations. No solution found.')
	return None
  
f = lambda x: x**3+3*(x**2)-1
df = lambda x: 3*(x**2)+6*x

newton(f,df,3/4,10e-4,15)