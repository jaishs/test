# 7.Write a function using list-comprehension to create a list of numbers which are divisible by 3
#  example input [1, 3, 5, 9, 11, 12, 20, 15, 50, 33]
def div3(d3):
    x = [i for i in d3 if i % 3 == 0]
    return x
d3=[1, 3, 5, 9, 11, 12, 20, 15, 50, 33]
print("num div by 3 is",div3(d3))