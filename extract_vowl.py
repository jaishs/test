# 10.Python function to remove  vowels in a given word
strg = "hello this is a test this is"
vowels = ["a", "e", "i", "o", "u"]
x=list(strg)
print(x)
for i in x:
    if i in vowels:
        x.remove(i)
print(x)
