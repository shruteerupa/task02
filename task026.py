def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def multplication(a,b):
    return a*b
def div(a,b):
    return a/b
print('1=addition')
print('2=substraction')
print('3=multplication')
print('4=division')
while True:
    choice=int(input('enter 1,2,3,4:'))
    if choice in (1,2,3,4):
        n1=float(input('enter the first num:'))
        n2=float(input('enter the second num:'))
        if choice==1:
            print('sum=',sum(n1,n2))
        elif choice==2:
            print('difference=',sub(n1,n2))
        elif choice==3:
            print('product=',multplication(n1,n2))
        elif choice==4:
            print('divison=',div(n1,n2))
        break
    else:
        print('invalid input')