
def max_num(num1, num2, num3):
    if num1 != num2 and num1 != num3 and num2 != num3:
        print("All numbers are different")
        
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("Max number is", max_num(300,6,1))