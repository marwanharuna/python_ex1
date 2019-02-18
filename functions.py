# WAP for functons of factorial and prime numbers

def factorial(num):
	sum = num
	i = 1
	for i in range(i,num):
		sum = sum * i
	return(sum)
def prime(num):
	i = 2
	check = 0
	for i in range(i,num+1):
		if(num % i == 0):
			return(1)
		else:
			check = check+1
			return(2)


