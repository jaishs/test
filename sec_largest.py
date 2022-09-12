# 6.Wite a function to find second largest number in a list

def seclar(a):
    m1=a[0]
    for i in a:
        if i>m1:
            m1=i
    m2=a[0]
    for i in a:
        if i>m2 and i!=m1:
            m2=i
    return m2
a=[1,2,3,4,5]
print("sec max is",seclar(a))