# WAP to print prime numbers in a given range.

range_one = int(input("\n Enter start of prime Number:"))
range_two = int(input("\n Enter end of prime Number:"))

if range_two <= 3:
	print("\n The Prime Numbers Are 2 and 3")
elif range_one > 3 :
	i = 1
	check = 0
	for i in range(range_one,range_two) :
		prime = range_one
		if prime % i == 0:
			break
		else:
			print(prime)