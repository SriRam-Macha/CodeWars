def move_zeros(array):
    b,c = [],[]
    for i in range(len(array)):
        if array[i] == (0 or 0.0) and not(array[i] is False) :
            b.append(int(array[i]))
        else:
            c.append(array[i])
    return (c+b)