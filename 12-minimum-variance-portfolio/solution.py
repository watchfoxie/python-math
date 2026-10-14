import numpy as np


def main():
    n = int(input())
    mu = np.array([float(token) for token in input().split()])
    cov = np.array([[float(token) for token in input().split()] for _ in range(n)])
    target = float(input())
    ones = np.ones(n)
    kkt = np.zeros((n + 2, n + 2))
    kkt[:n, :n] = 2.0 * cov
    kkt[:n, n] = ones
    kkt[:n, n + 1] = mu
    kkt[n, :n] = ones
    kkt[n + 1, :n] = mu
    rhs = np.zeros(n + 2)
    rhs[n] = 1.0
    rhs[n + 1] = target
    weights = np.linalg.solve(kkt, rhs)[:n]
    variance = float(weights @ cov @ weights)
    print(" ".join(f"{w:.6f}" for w in weights))
    print(f"{variance:.6f}")
    print(f"{variance ** 0.5:.6f}")


if __name__ == "__main__":
    main()
