def rot13(message):
    str = ""
    for c in message:
        if (ord(c) >= 65 and ord(c) <= 77) or (ord(c) >= 97 and ord(c) <= 109 ):
            aux = ord(c) + 13
            str +=  chr(aux)
        elif (ord(c) >= 78 and ord(c) <= 90) or (ord(c) >= 98 and ord(c) <= 122 ):
            aux = ord(c) - 13
            str += chr(aux)
        else: str+=c
    return str