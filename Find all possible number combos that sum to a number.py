def combos(n):
    result = []
    for p in lex_partitions(n):
        p = sorted(list(p))
        result.append(p)
    result = sorted(result)
    return result
def lex_partitions(n):
    if n == 0:
        yield []
        return
    for p in lex_partitions(n - 1):
        p.append(1)
        yield p
        p.pop()
        if len(p) == 1 or (len(p) > 1 and p[-1] < p[-2]):
            p[-1] += 1
            yield p
            p[-1] -= 1