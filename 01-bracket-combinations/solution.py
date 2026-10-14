from math import comb


def count_balanced(n):
    return comb(2 * n, n) // (n + 1)


def main():
    n = int(input().strip())
    print(count_balanced(n))


if __name__ == "__main__":
    main()
