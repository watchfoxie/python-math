def parens_balanced(text):
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return 0
    return 1 if depth == 0 else 0


def main():
    print(parens_balanced(input()))


if __name__ == "__main__":
    main()
