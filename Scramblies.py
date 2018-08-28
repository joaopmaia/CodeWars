def scramble(s1, s2):
    if(len(s1) < len(s2)): return False 
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    ind = 0
    from itertools import groupby
    c = [''.join(grp) for num, grp in groupby(s2)]
    for x in c:
        ind = s1.find(x, ind)
        if(ind == -1): return False 
    return True