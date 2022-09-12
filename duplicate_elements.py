# 5.write a function to print duplicate elements in the list
l=[1,2,3,3,4,4,4,5]
dup = []
for i in l:
    if l.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)
