def rgb(r, g, b):
    limit = lambda x: min(255, max(0, x)) 
    return '%02X%02X%02X' % (limit(r),limit(g),limit(b))