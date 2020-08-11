from array import *

testArray = array('i',[10,20,30,40,50])
testArray1 = [1,5,9,'llll']

for x in testArray:
    print(x)

testArray.insert(1,35)

for x in testArray:
    print(x)

testArray.remove(40)

for x in testArray:
    print(x)

print(testArray.index(35))

testArray[1] = 80

del testArray[1]

for x in testArray:
    print(x)

for x in testArray1:
    print(x)





