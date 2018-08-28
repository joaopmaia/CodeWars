def zeros(n):
    y=0
    while n > 1:
        n = int( n/5)
        y += n
    return y