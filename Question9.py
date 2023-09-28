import random

def summation(x):
    if len(x)==0:
        return 0

    return x[-1] + summation(x[:-1])


def normalize(x,summation):
    Sum = summation(x)
    for i in range(len(x)):
        x[i] = Sum - x[i]




numbers = random.randint(0, 20) #assume number of elements will be in range of 20
x=[]
for i in range(numbers):
    x.append(random.uniform(1.0, 10.0))
normalize(x, summation)
print(x)
