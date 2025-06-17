words = []
for _ in range(5):
    words.append(input('So‘z kiriting: '))
palindromes = []
for word in words:
    if word == word[::-1]:
        palindromes.append(word)
print(palindromes)
