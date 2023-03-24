print('''Практична робота №6.
Спітковська Владислава. Прикладна математика
''')
import random
set_list = int(input("Задати кількість підсписків:"))
data = []
list_general = []
for generate in range(set_list):
    list = random.sample(range(0, 3), 3)
    list_general.append(list)


def checker2(list):
    for i, sample_item in enumerate(list):
        print("Sample:", i, sample_item)
        for j, item in enumerate(list[i+1:], start=i+1):
            print("\tItem:", j, item)
            if item == sample_item:
                print("Remove element #" + str(j))
                list.pop(j)
    return list

print("Згенеруємо list, що буде складатись з {} трьоелементних листів:".format(set_list), list_general)
print("List:", checker2(list_general))

""" def checker(list_general, data):
    data += list_general
    check_point = 0
    for i in range(len(data)):
        while check_point < len(list_general):
            if data[i] == list_general[check_point] and i != check_point:
                print("Було знайдено і видалено дублікат під індексом {}".format(check_point))
                del list_general[check_point]
            else:
                check_point += 1
    return list_general 

print("Згенеруємо list, що буде складатись з {} трьоелементних листів:".format(set_list), list_general)

# print(checker(list_general, data))"""
