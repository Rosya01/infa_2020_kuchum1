def SpdStep(a, n):
    return (1 if n == 0
            else SpdStep(a * a, n // 2)
            if n % 2 == 0
            else a * SpdStep(a, n - 1))


def main():
    a = int(input())
    n = int(input())
    print(SpdStep(a, n))
if __name__ == "__main__":
    main()
