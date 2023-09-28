def capitalize(x):
    List = []
    for i in x:
        List.append(i.capitalize())

    x = tuple(List)
    return x

x = ('hello','functional','programming')
print(capitalize(x))
