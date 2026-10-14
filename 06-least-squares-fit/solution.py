import numpy as np


def fmt(value):
    if abs(value) < 1e-12:
        value = 0.0
    return f"{value:.6f}"


def main():
    m, d = map(int, input().split())
    xs = []
    ys = []
    for _ in range(m):
        x, y = map(float, input().split())
        xs.append(x)
        ys.append(y)
    x = np.array(xs)
    y = np.array(ys)
    design = np.column_stack([x ** power for power in range(d + 1)])
    coefficients = np.linalg.lstsq(design, y, rcond=None)[0]
    fitted = design @ coefficients
    residual = float(np.sum((y - fitted) ** 2))
    total = float(np.sum((y - y.mean()) ** 2))
    r_squared = 1.0 - residual / total
    rmse = (residual / m) ** 0.5
    print(" ".join(fmt(float(c)) for c in coefficients))
    print(fmt(r_squared))
    print(fmt(rmse))


if __name__ == "__main__":
    main()
