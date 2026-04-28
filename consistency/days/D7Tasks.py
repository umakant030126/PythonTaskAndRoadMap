# 📅 DAY 7 (Lists)
# 36. Find all pairs with given sum

def find_pairs_with_sum(lst , target_num):
    seen = set()
    pairs =[]
    for num in lst:
        complement = target_num - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

print(find_pairs_with_sum([1, 5, 7, -1, 5], 6))


# 37. Move all zeros to end

# Method 1
nums = [0,1,0,3,12]
print(nums)
nums[:] = [x for x in nums if x != 0] + [x for x in nums if x == 0]
print(nums)

# Method 2
def moveZero(lst):
    next_non_zero = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[next_non_zero] , lst[i] =  lst[i] ,  lst[next_non_zero]
            next_non_zero +=1
    return lst

print(moveZero([0,1,0,3,12]))


# 38. Find duplicate elements
def getDuplicateInList(lst):
    op = {}
    for i in range(len(lst)):
        if lst[i] not in op:
            op[lst[i]] = 1
        else:
            op[lst[i]] = op[lst[i]]+1

    print(op)
    op_key = []

    op_value = op.values()
    print(op_value)
    for num in op_value:
        if num > 1:
            op_key = [k for k,v in op.items() if v >1]

    return op_key


print(f"These number are more than one time in list :-> {getDuplicateInList([1,6,9,7,9,2,4,7,9])}")


