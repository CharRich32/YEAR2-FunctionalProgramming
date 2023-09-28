def lazy(numbers):
    for x in numbers:
        if x%3==0 and x%5==0:
            print('({}, FizzBuzz)'.format(x))
        elif x%3==0:
            print('({}, Fizz)'.format(x))
        elif x%5==0:
            print('({}, Buzz)'.format(x))
        else:
             print('({}, None)'.format(x))


#numbers from 1 to 100
numbers = [i for i in range(1,101)]
lazy(numbers)
