list1 = [1, 2, 3]
list2 = [4, 5, 6]
for i in range(len(list1)):
    list1[i], list2[i] = list2[i], list1[i]
print('List1:', list1)
print('List2:', list2)
