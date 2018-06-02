name = 'Ida'
names = ['Ida', 'Anna', 'Maria']

def hi(name):
    if name == 'Anna':
        print(name)
    else:
        print('not Anna')

#hi('Ida')

for name in names:
    hi(name)

