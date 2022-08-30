from multiprocessing.sharedctypes import Value


def prime (n):
    for i in range(3, n):
        if (n%i) == 0:
            return True
volue = prime (9)


print(Value)