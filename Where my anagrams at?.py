def anagrams(word, words):
    list = []
    list1 = []
    final =[]
    for x in range(0, len(word)):
        list.append(word[x])
    list.sort()
    for y in words:
        for w in range(0,len(y)):
            list1.append(y[w])
        list1.sort()
        if list1 == list:
            final.append(y)
        list1.clear()
    return final