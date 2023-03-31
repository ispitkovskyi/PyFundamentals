

intVar = 1
listVar = ["a", "b", "c"]

print("intVar before calling function = ", str(intVar))
print("listVar before calling function = ", listVar)
def callByCheck(immutableArg: int, mutableArg: list):
    immutableArg = immutableArg + 10
    mutableArg.reverse()
    mutableArg.extend(["d", "e", "f"])
    print("immutableArg inside function = ", str(immutableArg))
    print("mutableArg inside function = ", mutableArg)

callByCheck(intVar, listVar)

print("intVar after calling function (NOT CHANGED) = ", str(intVar))
print("listVar after calling function (CHANGED) = ", listVar)