def scramble(s1, s2):
    coll = {}
    for s in s1:
        if s in coll:
            coll[s] += 1
        else:
            coll.setdefault(s, 1)
    for s in s2:
        if s not in coll:
            return False
        coll[s] -= 1
        if coll[s] < 0:
            return False
    return True