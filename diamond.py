def diamond1(n):
    i = 0
    while i <= n:
        j = 0
        k = 0
        while j <= n-i:
            print(" ", end=" ")
            j = j + 1
        while k <= 2*i:
            print("*", end=" ")
            k = k + 1
        print(" ")
        i = i + 1

def diamond2(n):
    i = 0
    while i <= n:
        j = 0
        k = 0
        while k <= n-i:
            print("*", end=" ")
            k = k + 1
        while j <= i:
            print(" ", end=" ")
            j = j + 1
        print(" ")
        i = i + 1

diamond1(3)
diamond2(3)