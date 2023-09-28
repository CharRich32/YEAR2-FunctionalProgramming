def maximum(x):
    if len(x)==1:
        return x[0]
    
    Max = maximum(x[1:])
    if Max>x[0]:
        return Max
    else:
        return x[0]

def minimal(x):
    if len(x)==1:
        return x[0]
    
    Min = minimal(x[1:])
    if Min<x[0]:
        return Min
    else:
        return x[0]
        
def mean(x):
    if len(x)==1:
        return x[0]
    
    return (x[0] + (len(x)-1) * mean(x[1:])) / len(x)

def standard_deviation(x):
    return (sum((i-mean(x))**2 for i in x)/len(x))**0.5

x = [6.37,6.39,98.56,38.83,69.03,4.17,62.72,53.69,96.19,19.57,92.31,46.5,87.18,20.9,12.39]
print('Maximum:',maximum(x))
print('Minimal:',minimal(x))
print('Mean:',mean(x))
print('Standard deviation:',standard_deviation(x))
