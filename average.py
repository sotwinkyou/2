f = open('average.txt')
s = f.readline()
rez = ''
for i in s:
    rez = rez+str(ord(i))
print(rez)
