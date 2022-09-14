# 5.write a function to print duplicate elements in the list
# l=[1,2,3,3,4,4,4,5]
# dup = []
# for i in l:
#     if l.count(i)>1 and i not in dup:
#         dup.append(i)
# print(dup)

#or with using set function
l=[33,44,34,33,67,78,23,67]
print(list(set(l)))
