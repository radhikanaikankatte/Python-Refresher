x = lambda x : 2 * x
print(x(9))


max_xy = lambda x,y : x if x > y else y
print(max_xy(4,7))

mapA = map(lambda x: 3*x, [2,3,4])
print(list(mapA))

from functools import reduce

x = reduce(lambda x,y: x+y+2, [2,3,4])
print(x)

filteredList = list(filter(lambda x: x>2, [2,2,4,5,1,9]))
print(filteredList)

print(reduce(lambda x,y : x if x>y else y, [2,2,4,5,1,9]))

x = set(["Postcard", "Radio", "Telegram"])
y = set(["Radio","Television"])
print( x.difference(y) )
print( y.difference(x) )