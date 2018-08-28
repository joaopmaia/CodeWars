def find_outlier(integers):
    
    if integers[0]%2 == 0:
        if integers[1]%2 == 0:
            for x in range(0, len(integers),1):
                if (integers[x]%2 != 0):
                    return integers[x]
        else: 
            if integers[2]%2 == 0:
                return integers[1]
    else:
        if integers[1]%2 != 0:
            for x in range(0, len(integers),1):
                if integers[x]%2 == 0:
                    return integers[x]
        else:
            if integers[2]%2 != 0:
                return integers[1]
                
    if (integers[1]%2 == integers[2]%2 and integers[1]%2 != integers[0]):
        return integers[0]
        