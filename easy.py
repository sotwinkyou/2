f = open('easy.txt')
rez = ''
for i in f:
    rez = rez+chr(int(i))
print(rez)
