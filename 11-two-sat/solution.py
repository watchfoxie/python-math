def solve(n, clauses):
    size = 2 * n
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]
    for a, b in clauses:
        la = 2 * (a - 1 if a > 0 else -a - 1) + (a < 0)
        lb = 2 * (b - 1 if b > 0 else -b - 1) + (b < 0)
        adj[la ^ 1].append(lb)
        adj[lb ^ 1].append(la)
        radj[lb].append(la ^ 1)
        radj[la].append(lb ^ 1)
    order = []
    visited = [False] * size
    for start in range(size):
        if visited[start]:
            continue
        visited[start] = True
        stack = [(start, 0)]
        while stack:
            node, index = stack.pop()
            if index < len(adj[node]):
                stack.append((node, index + 1))
                nxt = adj[node][index]
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
    comp = [-1] * size
    count = 0
    for start in reversed(order):
        if comp[start] != -1:
            continue
        comp[start] = count
        stack = [start]
        while stack:
            node = stack.pop()
            for nxt in radj[node]:
                if comp[nxt] == -1:
                    comp[nxt] = count
                    stack.append(nxt)
        count += 1
    for v in range(n):
        if comp[2 * v] == comp[2 * v + 1]:
            return None
    return [1 if comp[2 * v] > comp[2 * v + 1] else 0 for v in range(n)]


def main():
    n, m = map(int, input().split())
    clauses = [tuple(map(int, input().split())) for _ in range(m)]
    values = solve(n, clauses)
    if values is None:
        print("unsatisfiable")
    else:
        print("satisfiable")
        print(" ".join(map(str, values)))


if __name__ == "__main__":
    main()
