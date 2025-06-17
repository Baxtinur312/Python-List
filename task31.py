lst = [3, 5, 3, 2, 5, 5, 1]
max_count = 0
most_common = None
for item in lst:
    count = lst.count(item)
    if count > max_count:
        max_count = count
        most_common = item
print(most_common)
