q = int(input('enter a no:'))
f =1
if q<0:
    pass
else:
    for i in range(1,q+1):
        f = f*i
print("The factorial is :",f)
