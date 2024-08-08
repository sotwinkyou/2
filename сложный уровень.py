f = open('hard.txt')
kl = 0
for i in f:
    if ord('L')==int(i):
        kl+=1
if kl>=5:
    print('LOVE')
else:
    print('PAIN')
