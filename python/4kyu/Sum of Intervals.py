import numpy as np
def sum_of_intervals(intervals):
    a = np.amax(intervals)
    b = np.amin(intervals)
    if b < 0:
        lis = [0]*((a - b) + 1)
        for i in intervals:
            for j in range(i[0] + abs(b), i[1] + abs(b)):
                lis[j] = 1
        return(sum(lis))
    else:
        lis = [0]*(a+2)
    for i in intervals:
        for j in range(i[0], i[1]):
            lis[j] = 1
    return(sum(lis))