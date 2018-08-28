def solution(number):
    list = []
    soma = 0
    for x in range(number - 1, 0, -1):
        print(x)
        if (x%3 == 0) or (x%5 == 0):
            list.append(x)
    for y in list:
        soma += y
    print (soma)
    return soma