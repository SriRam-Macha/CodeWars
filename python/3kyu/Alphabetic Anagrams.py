from math import factorial as fact
from collections import Counter
from numpy import prod


def listPosition(word):
    order = sorted(word)
    wordcount = dict(Counter(order))
    n = len(word)

    rank = 1
    for i in range(n):
        # Number of remmaining characters lesser than word[i]
        less = order.index(word[i])
        # Factorials for Denominator
        d_count = [fact(wordcount[j]) for j in set(word[i:])]
        rank += less*fact(n - i - 1)//prod(d_count)

        # Removing the current character
        order.remove(word[i])
        wordcount[word[i]] = max(0, wordcount[word[i]] - 1)

    return rank