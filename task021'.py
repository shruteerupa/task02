def outerFun(a, b):

    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5
first=int(input('enter the numb'))
second=float(input('enter the numb'))
result=outerFun(first,second)
print(result)