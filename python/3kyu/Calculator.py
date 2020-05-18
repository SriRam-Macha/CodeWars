from collections import Counter
class Calculator(object):
  def evaluate(self, string):
    L = string.split()
    CL = dict(Counter(L[1::2]))
    for _ in range(CL.get('/',0)):
        I = L.index('/')
        E = float(L[I - 1]) / float(L[I+1])
        del(L[I - 1 :I + 2])
        L.insert(I-1,E)
    for _ in range(CL.get('*',0)):
        I = L.index('*')
        E = float(L[I - 1]) * float(L[I+1])
        del(L[I - 1 :I + 2])
        L.insert(I-1,E)
    for _ in range(CL.get('-',0)):
        I = L.index('-')
        E = float(L[I - 1]) - float(L[I+1])
        del(L[I - 1 :I + 2])
        L.insert(I-1,E)
    for _ in range(CL.get('+',0)):
        I = L.index('+')
        E = float(L[I - 1]) + float(L[I+1])
        del(L[I - 1 :I + 2])
        L.insert(I-1,E)
    if (float(L[0])%1==0):
        return (int(L[0]))
    else:
        return (float(L[0]))