PHI = (5 ** 0.5 - 1) / 2


def evaluate(coefficients, x):
    value = 0.0
    for c in coefficients:
        value = value * x + c
    return value


def main():
    degree = int(input())
    coefficients = [float(token) for token in input().split()]
    left, right = map(float, input().split())
    c = right - PHI * (right - left)
    d = left + PHI * (right - left)
    fc = evaluate(coefficients, c)
    fd = evaluate(coefficients, d)
    while right - left > 1e-9:
        if fc < fd:
            right, d, fd = d, c, fc
            c = right - PHI * (right - left)
            fc = evaluate(coefficients, c)
        else:
            left, c, fc = c, d, fd
            d = left + PHI * (right - left)
            fd = evaluate(coefficients, d)
    x_star = (left + right) / 2
    print(f"{x_star:.6f}")
    print(f"{evaluate(coefficients, x_star):.6f}")


if __name__ == "__main__":
    main()
