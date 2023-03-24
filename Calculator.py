
num1 = float(input("First number: "))
op = input("Enter operator: ")
num2 = float(input("Second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Error: Invalid operator used")