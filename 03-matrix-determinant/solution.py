from fractions import Fraction


def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot_row = max(range(col, n), key=lambda r: abs(a[r][col]))
        if a[pivot_row][col] == 0:
            return Fraction(0)
        if pivot_row != col:
            a[col], a[pivot_row] = a[pivot_row], a[col]
            det = -det
        pivot = a[col][col]
        det *= pivot
        for r in range(col + 1, n):
            factor = a[r][col] / pivot
            if factor:
                for c in range(col, n):
                    a[r][c] -= factor * a[col][c]
    return det


def format_result(value):
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main():
    n = int(input().strip())
    matrix = []
    for _ in range(n):
        matrix.append([Fraction(token) for token in input().split()])
    print(format_result(determinant(matrix)))


if __name__ == "__main__":
    main()
