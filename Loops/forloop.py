
for letter in "Giraffe Academy":
    print(letter)

print("#################################")

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

print("#############  ##########")
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first iteration")

print("########## iterate by range of indexes, having custom start index specified ###############")
for index in range(2, 10):
    print(index)
print("########### iterate by range of indexes use custom step ######################")
for index in range(2, 10, 2):
    print(index)

print("########### iterage through array using index provided by range() ######################")
for index in range(len(friends)):
    print(friends[index])

