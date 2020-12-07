def sum(a, b):
    return (sum(a + 1, b - 1) if b else a)


def main():
    a = int(input())
    b = int(input())
    print(sum(a, b))
if __name__ == "__main__":
    main()
