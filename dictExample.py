dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
#print("dict['dfsdf']: ", dict['Agsdfsdfe'])

#iterate fails
# for x in dict.items:
#     print(x)

#print(dict.items)

dict['Age'] = 15
print("dict['Age']: ", dict['Age'])

dict['School'] = 'holy convent'
print("dict['School']: ", dict['School'])

print("dict['Class']: ", dict['Class'])
del dict['Class']
# print("dict['Class']: ", dict['Class'])

dict.clear()
#del dict

# Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example

dict[(1,2)] = 'Alice'
print(dict[(1,2)])

for x in dict.keys():
    print(x)

for x in dict.values():
    print(x)

for x in dict.items():
    print(x)


