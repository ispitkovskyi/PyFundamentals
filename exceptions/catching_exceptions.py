
try:
    number = float(input("Enter a number: "))
    print(number)
    dividor = float(input("Enter a value to divide the number: "))
    print(number/dividor)
except ValueError as err:    
    print("Ivalid input problem:", err)    
except ZeroDivisionError as err:
    print("Division by zero problem:", err)
except:
    print("Any type of error is cought (bad practice)")

