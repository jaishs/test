#  1. Write a function to find sum of the list elements
#     Ex: Input [12,2,46]
#     output = 60

def additn(a):
    c=0
    for i in a:
        c=c+i
    return c
a=[12,2,4]
print("sum is",additn(a))

# def additn(a):
#     c=sum(a)
#     return c
# a=list(map(int,input("enter list ele").split()))
# print(a)
# print("sum is",additn(a))
