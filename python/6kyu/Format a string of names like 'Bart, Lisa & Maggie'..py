def namelist(names):
    if len(names) == 0 :
        return ''
    b = []
    for i in names:
      for k in i.items():
        b.append(k)
    if len(b) == 1:
        return str(b[0])
    b.insert(-1,'&')
    return (', '.join(b[:-2]) +' '+ ' '.join(b[-2:]))