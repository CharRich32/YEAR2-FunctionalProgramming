def convert_characters(x):
    for i in range(len(x)):
        if x[i].isupper():
            x = x[:i] + x[i].lower() + x[i+1:]
        elif x[i].islower():
            x = x[:i] + x[i].upper() + x[i+1:]

    return x


x='Hello, World!'
print(convert_characters(x))
