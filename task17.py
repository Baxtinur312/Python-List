names = []
while True:
    name = input('Ism kiriting (yoki stop): ')
    if name == 'stop':
        break
    names.append(name)
print('Umumiy ismlar soni:', len(names))
