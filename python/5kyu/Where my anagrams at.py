def anagrams(word, words):
    b = []
    for i in words:
        if len(word) == len(i):
            if set(word) == set(i):
                b.append(i)
    return b