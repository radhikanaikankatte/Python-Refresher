def sum(list):
    sum = 0
    for x in range(0,len(list)):
        sum = sum + list[x]
    
    return sum

def sumRecursion(list):
    if len(list) == 1:
        return list[0]
    
    return list[0] + sumRecursion(list[1:])

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def fibGen():
    a, b = 1,1
    while 1:
        yield a

        a,b = b, a+b

print(sum([5,7,3,8,10]))
print(sumRecursion([5,7,3,8,10]))

print(factorial(3))
print(factorial(5))

print(fibonacci(12))

count = 0
for x in fibGen():
    print(x)
    count += 1
    if (count == 5):
        break

