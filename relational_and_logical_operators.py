# WAP for relational and logical operators.

marks = int(input("Enter marks:"))

if marks == 100:
	print("Outstanding, obtained complete marks")
elif marks < 100 and marks >= 90 :
	print("Excellent!!!")
elif marks < 90 and marks >= 80:
	print(" Very Good!!!!")
elif marks > 50 or marks < 80 and marks >= 50:
	print("Pass")
elif marks < 50 :
	print("Fail")
else :
	print("invalid marks!!!")

print("You did not attempt exam: ", not marks)