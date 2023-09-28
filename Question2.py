def headsAndTails(x):
    for i in x:
        print('head',i,end='\ttail ')
        x = x[1:]
        print(x)


x = [0,1,2,3,4]
headsAndTails(x)
