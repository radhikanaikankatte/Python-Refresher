def bubblesort(list):
    isSorted = False
    lastElement = len(list)-1
    while not isSorted:
        isSorted = True
        for x in range(0, lastElement):
            if list[x] > list[x+1]:
                swap(list, x, x+1)
                isSorted = False
        lastElement -= 1

def swap(list, left, right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp

def bubblesortAlt(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)

list = [19,2,31,45,6,11,121,27]
bubblesortAlt(list)
print(list)
