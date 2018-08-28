def tickets(people): 
    count25 = 0
    count50 = 0
    print (people)
    for x in range(0, len(people),1):
        if people[x] == 25:
            count25 += 1 
        elif people[x] == 50:
            if count25 > 0:
                count25 -= 1
                count50 +=1
            else:
                return "NO"
        elif people[x] == 100:
            
            if (count25 > 0 and count50 > 0):
                count25 -=1
                count50 -=1
            elif (count25 > 2):
                count25 -= 3
            else:
                return "NO"
    return "YES"