def prime(n):
    flag = True
    for i in range(2, n):
        if (n % i) == 0:
            flag = False
            break
    if flag:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

prime(int(input("enter the number")))