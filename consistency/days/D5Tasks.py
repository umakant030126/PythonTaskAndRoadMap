## Day 5
# 21. Max/min in list
lst1 = [3,7,9,4,2,5,9,2,6,8]
print("Maximum number in list is : ",max(lst1))
print("Minimum number in list is : ",min(lst1))


#22. Remove duplicates
# method 1 -  order not maintain
uniqueLst = list(set(lst1))
print(uniqueLst)
print(type(uniqueLst))

# method 2 -  order maintain
uniqueLst2= list(dict.fromkeys(lst1))
print(uniqueLst2)

print("********************")

# 23. Manual sort
lst2 =uniqueLst2
print(lst2)

itemCount = len(lst2)

for i in range(itemCount):
    for j in range(0,itemCount-i-1):
        if lst2[j] > lst2[j+1]:
            lst2[j] , lst2[j+1] = lst2[j+1] , lst2[j]

print(f"Sorted list is : {lst2}")




# 24. Merge lists
list1 = [1,3,5,7]
list2 = [2,4,6,8]

# method 1
mergeList = list1 + list2
print(mergeList)

# method 2
for i in list2:
    list1.append(i)

print(list1)




# 25. Second largest
highest = secondHighest = float('-inf')
print(f'Highest number is : {highest}')

for num in lst1:
    if num > highest:
        secondHighest = secondHighest
        highest = num
    elif num >secondHighest and num != highest:
        secondHighest = num

print(lst1)
print(f"Highest in list is {max(lst1)}")
print(f"Second highest in list is {secondHighest}")

