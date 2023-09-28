def Split(x):
    x1 = []
    x2 = []
    for i in x:
        if i%2==0:
            x1.append(i)
        else:
            x2.append(i)

    print('x1 =', x1)
    print('x2 =', x2)


x = [1,2,3,4,5,6,7,8,9,10]
Split(x)            
