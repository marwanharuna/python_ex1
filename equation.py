# program of all mighty formula
import math
a = int(input("Enter the value of A:"))
b = int(input("Enter the value of B:"))
c = int(input("Enter the value of C:"))

discriminant = (b*b) - (4*a*c)

if discriminant == 0 :
	print("Roots are equal.")
elif discriminant < 0 :
	print("Roots are complex")
else :
	root1=(-b)+math.sqrt((b*b)-(4*a*c))/2*a
	root2=(-b)-math.sqrt((b*b)-(4*a*c))/2*a
	print("\n Alpha is:",root1,"and Beta is:",root2)