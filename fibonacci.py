# WAP to print the fibonacci series

num = int(input("Enter a number:"))

if num <= 1:
	print("Numbers less than or equals to one are invalid")

elif num > 1:
	a = 0;
	b = 1;
	if num == 2:
		print(a)
	else:
		i = 0
		print(a)
		print(b)
		for i in range(i,num-2):
			c = b+a
			print(c)
			a = b
			b = c
else:
	print("Invalid input")
			