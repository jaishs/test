#8.Write a function to sort a list without using sort function

def srt(a):
    x = []
    while a:
        min = a[0]
        for i in a:
            if i < min:
                min = i
        x.append(min)
        a.remove(min)
    return x

a =[-15, -26, 15, 1, 23, -64, 23, 76]
print(srt(a))