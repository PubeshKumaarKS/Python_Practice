q = int(input())
c = 0
for i in range(q):
    if q%(i+1) == 0:
        c+=1
    else:
        pass

if c == 2:
    print('prime')
else:
    print('non - prime')
