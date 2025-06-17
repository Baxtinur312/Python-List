nums = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]
unique = []
for n in nums:
    if nums.count(n) == 1:
        unique.append(n)
print(unique)
