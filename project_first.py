# a simple project for basic python programs

print("*************WELCOME TO PYTHON PROGRAMS**************")
print("1.Arithmetic Calculator \n 2.Piggy Bank \n 3.Electricity Bill \n 4.CGPA\PERCENTAGE CALCULATOR \n 5.NET SALARY CALCULATOR")
choice = int(input("\n Enter choice"))
if choice == 1:
	print("Select Operation To Perform:")
	print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Modulos \n6.Exponent")
	option = int(input("Enter Value:"))
	num1 = int(input("Enter Fisrt Number:"))
	num2 = int(input("Enter Second Number:"))
	if option == 1:
		num3 = num1 + num2
		print("The Addition is:",num3)
	if option == 2:
		num3 = num1 - num2
		print("The Subtraction is:",num3)
	if option == 3:
		num3 = num1 * num2
		print("The Multiplication is:",num3)
	if option == 4:
		num3 = num1 / num2
		print("The Division is:",num3)
	if option == 5:
		num3 = num1 % num2
		print("The Modulus is:",num3)
	if option == 6:
		
		num3 = num1**num2
		print("The Exponent is:",num3)
	else:
		print("Invalid Option")
if choice == 2:
	ten_rupees = int(input("Enter Amount Of Ten Rupees Coins:"))
	five_rupees = int(input("Enter Amount Of Five Rupees Coins:"))
	two_rupees = int(input("Enter Amount Of Two Rupees Coins:"))
	one_rupees = int(input("Enter Amount Of One Rupees Coins:"))
	
	ten_rupees= ten_rupees * 10
	five_rupees= five_rupees * 5
	two_rupees= two_rupees * 2
	one_rupees= ten_rupees * 1
	
	total_amount = ten_rupees + five_rupees + two_rupees + one_rupees
	print("******************************")
	print("Amount In Piggy Bank Is:",total_amount)
	print("******************************")
if choice == 3:
	meter = float(input("\n Enter Meter Reading:"))
	if meter >= 100:
		meter = meter * 6.95
		print("******************************")
		print("Electricity Bill Is:", meter)
		print("******************************")
	if meter < 100:
		meter = meter * 5.95
		print("******************************")
		print("Electricity Bill Is:", meter)
		print("******************************")	
	else:
		print("\n Invalid Reading!!!")
if choice == 4:
	print("\n1.CGPA \n 2.PERCENTAGE")
	sel = int(input("Enter Operation To Perform"))
	if sel == 1:
	ca_marks = float(input("\n Enter c a marks:"))
	attendance_marks = float(input("\n Enter attendance marks:"))
	midterm_marks = float(input("\n Enter midterm marks:"))
	endterm_marks = float(input("\n Enter endterm marks:"))

	new_ca_marks = ca_marks/30
	new_ca_marks = new_ca_marks * 25
	new_midterm_marks = midterm_marks/2
	new_endterm_marks = endterm_marks/70
	new_endterm_marks = new_endterm_marks * 50

	total_marks = attendance_marks + new_ca_marks + new_endterm_marks + new_endterm_marks
	print("\n PERCENTAGE IS :", total_marks)
	if sel == 2:
	percentage = float(input("\n Enter percentage:")
	cgpa = percentage/10
	print("\n Your CGPA is :", cgpa)
if choice == 5:
	salary = float(input("\nEnter Salary:"))
	working_days = float(input("\nEnter Working days:"))
	house_Allowance = float(input("\n Enter House Allowance:"))
	exact_salary = salary * working_days
	gross_salary = exact_salary + house_allowance
	tax = gross_salary * 0.1
	net_salary = gross_salary - tax
	print("Salary for ", working_days , " is ", net_salary)