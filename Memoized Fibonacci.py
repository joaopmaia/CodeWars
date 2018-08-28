def fibonacci(n):
    if n in [0, 1]:
        return n
    a,b=0,1
    for i in range(0,n-1):
        b=a+b
        a=b-a
    return b
        