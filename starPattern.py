print('Star Pattern')
print(' ')
for i in range(-6,7,1):
    a=abs(i)
    for j in range(-6,7,1):
        b=abs(j)
        if a==b or a==6 or b==6 or (a<=3 and b<=3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()