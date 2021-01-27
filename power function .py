def power(a, n):
	if n ==0:
		return 1
	else:
		return a * power(a,n - 1)
		
		
#test
a = power(7,2)
print(a)