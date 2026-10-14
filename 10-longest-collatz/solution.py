from array import array


def main():
    n = int(input())
    lengths = array("i", bytes(4 * (n + 1)))
    maxima = array("q", bytes(8 * (n + 1)))
    lengths[1] = 1
    maxima[1] = 1
    best_start = 1
    best_length = 1
    best_top = 1
    for k in range(2, n + 1):
        steps = 0
        v = k
        chain_max = k
        while v > n or lengths[v] == 0:
            if v % 2 == 0:
                v //= 2
            else:
                v = 3 * v + 1
            if v > chain_max:
                chain_max = v
            steps += 1
        total = steps + lengths[v]
        lengths[k] = total
        top = chain_max if chain_max > maxima[v] else maxima[v]
        maxima[k] = top
        if total > best_length:
            best_start = k
            best_length = total
            best_top = top
    print(best_start, best_length, best_top)


if __name__ == "__main__":
    main()
