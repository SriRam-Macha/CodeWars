def iq_test(numbers):
    odd =[]
    even=[]
    for i in [int(i) for i in numbers.split()] :
        odd.append(i) if i%2 else even.append(i)
    return 1 + [int(i) for i in numbers.split()].index(odd[0]) if len(odd) < 2 else 1 +[int(i) for i in numbers.split()].index(even[0])