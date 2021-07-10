

keys = ('a', 'b', 'c')
vals = ( 1,   2,   3 )
d = dict()
for key, val in zip(keys, vals):
    d[key] = val
    
print(d)