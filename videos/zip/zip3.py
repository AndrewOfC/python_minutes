
keys = ('a', 'b', 'c')
vals = ( 1,   2,   3 )
d = { k:v for k,v in zip(keys, vals) }
print(d)