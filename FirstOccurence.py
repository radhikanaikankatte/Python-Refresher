def getFirstPosition(s_list, target):
    if len(s_list) < 1:
        return "Invalid"
    
    if len(s_list) == 1:
        if s_list[0] == target:
            return 0
        else:
            return "value not found"

    left_index = 0
    right_index = len(s_list) - 1

    while left_index < right_index :
        mid_index =  (left_index + right_index)// 2

        if s_list[mid_index] >= target:
            right_index = mid_index

        else:
            left_index = mid_index + 1

    if s_list[left_index] == target:
        return left_index

def getFirstPosition2(s_list, target):
    if len(s_list) < 1:
        return "Invalid"
    
    if len(s_list) == 1:
        if s_list[0] == target:
            return 0
        else:
            return "value not found"

    left_index = 0
    right_index = len(s_list) - 1

    return getFirstPositionIndex2(s_list, left_index, right_index, target)

def getFirstPositionIndex2(s_list, left_index, right_index, target):
    if s_list[left_index] == target and left_index == right_index:
        return left_index

    if left_index < right_index :
        mid_index =  (left_index + right_index)// 2

        if s_list[mid_index] >= target:
            right_index = mid_index

        else:
            left_index = mid_index + 1

        return getFirstPositionIndex2(s_list, left_index, right_index, target)

    




print(getFirstPosition([1,2,3,5,7],3))
print(getFirstPosition2([1,5,5,4,9,9,9,12,14,14,100],14))




