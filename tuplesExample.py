tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
tup3 = (7,)
tup4 = (7)
 
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

print("Value available at index 2 : ")
print(tup1[2])
# tup1[2] = 2001
print("New value available at index 2 : ")
print(tup1[2])

# tup1.append("jjuuuu")
# tup1.insert(2, 76)
# tup1.remove(2000)
# pp = tup1.pop(3)

for x in tup1:
    print(x)

#print(pp)

# del tup1[2]

for x in tup1:
    print(x)

print(tup1 + tup2)

print(tup2 * 4)

if 6 in tup2:
    print("found 6")

print(str(tup1.count))

print(tup3)
print(tup4)
print(tup3+tup1)

print(tup1[2])

tup5 = tup2[1:5:2] + tup1[2:4]
print(tup2[1:5:2])

print(tup5)