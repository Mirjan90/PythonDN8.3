
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

arithemtic = input("Choose arithemtic operation (+, -, * or / ): ")

if arithemtic == "+":
    print(num_1 + num_2)

elif arithemtic == "-":
    print(num_1 - num_2)

elif arithemtic == "*":
    print(num_1 * num_2)

elif arithemtic == "/":
    print(num_1 / num_2)

else:
    print("Wrong arithemtic operation, try again!")