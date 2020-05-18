def unique_in_order(iterable):
    lis=[]
    if len(iterable) > 0:
        for i in range(len(iterable) - 1 ):
            if iterable[i] != iterable[i+1]:
                lis.append(iterable[i])
        lis.append(iterable[-1])
    return lis