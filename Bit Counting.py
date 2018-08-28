def countBits(n):
    aux = str(bin(n))
    count = 0
    for x in range(0, len(aux),1):
        if aux[x] == "1":
            count += 1
    return count