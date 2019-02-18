#WAP to check factorian and prime number with seperate file.

import functions
print("**********FACTORIAL AND PRIME NUMBERS**********")
print("1.FACTORIAL \n 2.PRIME NUMBER")
option = int(input("Enter Option:"))
num = int(input("Enter Value To Check:"))

if option == 1:
	result = functions.factorial(num)
	print(result)
elif option == 2:
	result = functions.prime(num)
	if result == 1:
		print("Not A Prime Number!!!")
	elif result == 2:
		print("A Prime Number!!!")
	else:
		print("Error Try Again")
else:
	print("Invalid Option")