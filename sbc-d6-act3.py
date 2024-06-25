n = int(input("Enter N:"))
for i in range(n, 0, -1):
    print("*" * i)
    if i == 2:
        rng = n - 2
        s = " "*rng
        print("*", end=s)
for j in range(2, n + 1):
    print("*" * j)