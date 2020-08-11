def mergeSort(list):
    if len(list) <= 1 :
        return list

    middle = len(list) // 2
    left_list = list[:middle]
    right_list = list[middle:]

    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)
    return mergeHalves(left_list, right_list)

def mergeHalves(left_half, right_half):
    res = []

    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])

        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    
    if len(left_half) == 0:
        res = res + right_half

    else:
        res = res + left_half
    
    return list(res)



unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(mergeSort(unsorted_list))



