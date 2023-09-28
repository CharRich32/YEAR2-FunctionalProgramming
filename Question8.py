def summation(x):
    if x==0:
        return x

    return x + summation(x-1)

def tail_summation(x,Sum=0):
    if x==0:
        return Sum

    return tail_summation(x-1,Sum+x)

print('Sum of the first 10 natural numbers using recursinon:',summation(10))
print('Sum of the first 10 natural numbers tail recursinon:',tail_summation(10))
