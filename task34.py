nums = [1, 2, 3, 7, 8, 9]
pairs = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 10:
            pairs.append((nums[i], nums[j]))
print(pairs)
