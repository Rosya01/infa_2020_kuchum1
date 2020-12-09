def rec():
    n = int(input())
    if n != 0:
        if n % 2 == 0 or n % 2 != 0:
            rec()
        print(n)
    else:
        print(n)
rec()
