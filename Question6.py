def printElements(x):
    if len(x)==0:
        return

    print(x[0],end=' ')
    printElements(x[1:])


x = ['a','b','c','d']
printElements(x)
