from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])

print(T[1][2])

for x in T:
    for y in x:
        print(y)

T.insert(2,[1,2,0])

for x in T:
    for y in x:
        print(y)

T.remove([15, 6,10])

for x in T:
    for y in x:
        print(y)

T[3] = [0,9,7]


for x in T:
    for y in x:
        print(y)

T[1][2] = 63


for x in T:
    for y in x:
        print(y)

del T[3]

for x in T:
    for y in x:
        print(y)
