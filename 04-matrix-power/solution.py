def multiply(a, b, m):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        row_a = a[i]
        row_r = result[i]
        for k in range(n):
            value = row_a[k]
            if value:
                row_b = b[k]
                for j in range(n):
                    row_r[j] = (row_r[j] + value * row_b[j]) % m
    return result


def main():
    n, k, m = map(int, input().split())
    base = []
    for _ in range(n):
        base.append([value % m for value in map(int, input().split())])
    result = [[1 % m if i == j else 0 for j in range(n)] for i in range(n)]
    while k > 0:
        if k & 1:
            result = multiply(result, base, m)
        k >>= 1
        if k:
            base = multiply(base, base, m)
    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
