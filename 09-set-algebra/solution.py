def read_set():
    return set(input().split())


def main():
    a = read_set()
    b = read_set()
    c = read_set()
    union = a | b | c
    intersection = a & b & c
    inclusion_exclusion = (
        len(a)
        + len(b)
        + len(c)
        - len(a & b)
        - len(a & c)
        - len(b & c)
        + len(a & b & c)
    )
    print("union", len(union), *sorted(union))
    print("intersection", len(intersection), *sorted(intersection))
    print("inclusion-exclusion", inclusion_exclusion)
    print("direct", len(union))
    print("agree" if inclusion_exclusion == len(union) else "disagree")


if __name__ == "__main__":
    main()
