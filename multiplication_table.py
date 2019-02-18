"""
# Multiplication table

i=1
n= int(input("Enter Number to get table:"))

for i in range(1,11):
	r = i*n
	print(i," x ",n,":",r)

# Factorial of a number

number = int(input("\n Enter number to find factorial"))

if number == 0:
	print("\n Factorial is 1")
elif number == 0:
	print("\n Factorial is 1")
elif number < 0:
	print("\n Number is not valid")
else :
	sum = 1
	i = 1
	for i in range(1,number) :
		sum = sum * number
		number = number - 1
	print(sum)
"""

# checking prime number

prime = int(input("\n Enter a prime Number:"))

if prime <= 0 :
	print("\n Number less than or equals to zero")
elif prime < 3:
	print("\n Number is Prime")
elif prime > 3 :
	i = 1
	check = 0
	for i in range(1,prime) :
		if prime % i == 0:
			check = check + 1
	if check == 1 :
		print("\n Number is prime")
	else :
		print("\n Number is not prime")
		