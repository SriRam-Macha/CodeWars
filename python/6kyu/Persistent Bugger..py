def persistence(n):
    counter=0
    while n>9:
        counter+=1
        num_str=str(n)
        total=1
        for i in num_str:
            total=total* int(i)
        n=total
    return counter