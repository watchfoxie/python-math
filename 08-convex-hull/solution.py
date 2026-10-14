def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def half_hull(points):
    chain = []
    for p in points:
        while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0:
            chain.pop()
        chain.append(p)
    return chain


def main():
    m = int(input())
    points = sorted(set(tuple(map(float, input().split())) for _ in range(m)))
    if len(points) == 1:
        hull = [points[0]]
    else:
        hull = half_hull(points)[:-1] + half_hull(points[::-1])[:-1]
    perimeter = 0.0
    for i in range(len(hull)):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % len(hull)]
        perimeter += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(len(hull))
    for x, y in hull:
        print(f"{x:g} {y:g}")
    print(f"{perimeter:.6f}")


if __name__ == "__main__":
    main()
