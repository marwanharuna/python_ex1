# testing bitwise operator

first_input = int(input("Enter first digit:"))
second_input = int(input("Enter second digit:"))

output = first_input & second_input
print("And operator of two inputs:", output)
output = first_input | second_input
print("Or operator of two inputs:", output)
print("Not operator of input:", ~first_input)
output = first_input ^ second_input
print("Xor operator of two inputs:", output)
output = first_input >> second_input
print("Right Shift operator of input:", output)
output = first_input << second_input
print("Left Shift operator of input:", output)