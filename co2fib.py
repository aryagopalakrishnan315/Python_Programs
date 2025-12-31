def fibonacci_series(n): 
	series = [] 
	a, b = 0, 1 
	for _ in range(n): 
		series.append(a) 
		a, b = b, a + b 
	return series 
n = int(input("Enter the limit: ")) 
fib_sequence = fibonacci_series(n) 
print("Fibonacci series:", fib_sequence) 
