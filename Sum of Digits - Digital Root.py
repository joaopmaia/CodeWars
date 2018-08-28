def digital_root(n):
    aux = str(n)
    soma = 0
    for x in range(0, len(aux)):
        soma += int(aux[x])   
    if len(str(soma)) > 1:
        soma = digital_root(soma)
    return soma