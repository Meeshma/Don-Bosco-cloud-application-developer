def pyramid(x):
    for i in range(x):
        for j in range(x - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

pyramid(19)
