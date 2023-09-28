def link_elements(x,sep):
    res = ""
    for i in x[:-1]:
        res+=i+sep

    return res+x[-1]

#Code for Q7.2
def split_elements(x,sep):
    res = x.split(sep)
    return res

x = ['hello','functional','programming']
sep = '---'

string = link_elements(x, sep) 
print('Link elements:',string)
print('Split elements:',split_elements(string, sep))
