keys = ( 'a', 'b', 'c', 'd', 'e', 'f' )
values = ( 0, 1, 2, 3, 4 )

dictionary = dict()
for key, value in zip(keys, values):
    dictionary[key] = value # 3 lines
    
print(dictionary) # Better!  ( but still not best )
