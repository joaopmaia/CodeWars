def rgb(r, g, b):
    arr =[r,g,b]
    final = ""
    for x in range(0,len(arr)):
        if arr[x] < 0:
            arr[x] = 0
        if arr[x] > 255:
            arr[x] = 255
        arr[x] = str(hex(arr[x])[2:]).zfill(2).upper()
        final += arr[x]
    print (final)
    return final