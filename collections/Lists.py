
lucky_numbers = [42, 4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Toby"]
print(friends)

#append one list to another
friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

print(friends.index("Oscar"))

print(friends.count("Jim"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

#remove last element from list
friends.pop()
print(friends)

friends2 = friends.copy()
print(friends2)

print("#################################################")
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", 2, True]
friends[1] = "Margot"
print(friends)
print(friends[1])
print(friends[2])
print(friends[-1]) #first from the end
print(friends[-2])
print(friends[1:3]) #elements with index 1, 2 (3 is not included)
