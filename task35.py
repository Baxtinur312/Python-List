words = ['AI', 'kitob', 'dasturlash', 'a', 'salom']
short = []
medium = []
long = []
for word in words:
    if len(word) <= 3:
        short.append(word)
    elif 4 <= len(word) <= 6:
        medium.append(word)
    else:
        long.append(word)
print('<=3:', short)
print('4-6:', medium)
print('>6:', long)
