def even(num):
    return num % 2 == 0
def odd(num):
    return num % 2 != 0
mylist = [1, 2, 3, 4, 5, 6, 7]
evenlist = []
oddlist = []
evenlist = list(filter(even, mylist))
oddlist = list(filter(odd, mylist))
print(evenlist)
print(oddlist)