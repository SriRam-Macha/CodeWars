def ips_between(start, end):
    diffrence = 0
    start,end = [int(i) for i in start.split(".")],[int(i) for i in end.split(".")]
    for i in range(4):
      diffrence += ((end[i]-start[i])*256**(3-i))
    return(diffrence)