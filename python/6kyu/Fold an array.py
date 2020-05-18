def fold_array(array, runs):
    a = 0
    b = []
    if len(array) % 2 == 0:
        for i in range(int(len(array)/2)):
            b.append(array[i] + array[-(i+1)])
    if len(array) % 2 == 1:
        for i in range(int(len(array)/2)):
            b.append(array[i] + array[-(i+1)])
        b.append(array[int(len(array)/2)])
    a += 1         
    if a == runs:
        return b
    else:
        return fold_array(b,(runs-1))