from math import isqrt


def base_primes(limit):
    if limit < 2:
        return []
    sieve = bytearray([1]) * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(range(i * i, limit + 1, i)))
    return [i for i in range(2, limit + 1) if sieve[i]]


def count_primes(lo, hi):
    primes = base_primes(isqrt(hi))
    size = hi - lo + 1
    window = bytearray([1]) * size
    for p in primes:
        start = max(p * p, ((lo + p - 1) // p) * p)
        if start > hi:
            continue
        window[start - lo :: p] = bytearray((hi - start) // p + 1)
    if lo == 1:
        window[0] = 0
    return sum(window)


def main():
    lo, hi = map(int, input().split())
    print(count_primes(lo, hi))


if __name__ == "__main__":
    main()
