def find_missing_letter(chars):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in chars:
        if  not(chars[(chars.index(i))+ 1] ==  s[s.index(i) + 1]) :
            return s[s.index(i) + 1]