def create_phone_number(n):
    aux = "("
    for x in range (0, 3, 1):
        aux +=  str(n[x])
    aux += ") "
    for x in range (3, 6, 1):
        aux += str(n[x])
    aux += "-"
    for x in range (6, 10, 1):
        aux += str(n[x])
    return aux