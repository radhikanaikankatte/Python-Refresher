list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

print("Value available at index 2 : ")
print(list1[2])
list1[2] = 2001
print("New value available at index 2 : ")
print(list1[2])

list1.append("jjuuuu")
list1.insert(2, 76)
list1.remove(2000)
pp = list1.pop(3)

for x in list1:
    print(x)

print(pp)

del list1[2]

for x in list1:
    print(x)

print(list1 + list2)

print(list2 * 4)

if 6 in list2:
    print("found 6")