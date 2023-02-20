
str1 = input("String1")
str2 = input("String2")

if len(str1) != len(str2):
    result = False
pattern1 = {}
pattern2 = {}
for i in range(len(str1)):
    if str1[i] not in pattern1:
        pattern1[str1[i]] = str2[i]
    else:
        if pattern1[str1[i]] != str2[i]:
            result = False
    if str2[i] not in pattern2:
        pattern2[str2[i]] = str1[i]
    else:
        if pattern2[str2[i]] != str1[i]:
            result = False
    result = True

print(result)