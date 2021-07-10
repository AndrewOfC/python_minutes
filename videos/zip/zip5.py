
lzip = lambda *a: list(zip(*a)) # acts like py2 zip
r = range(10)

l = lzip(r[0::2], r[1::2])
print(l)
