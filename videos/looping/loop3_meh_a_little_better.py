# loop through elements and make a dictionary

keys = ( 'a', 'b', 'c', 'd', 'e', 'f' )
values = ( 0, 1, 2, 3, 4 )

dictionary = dict()
for index, key in enumerate(keys): # meh.. a little better
    if index >= len(values):
        break 
    dictionary[key] = values[index] # 
    index += 1 # 7 lines
    
print(dictionary) 



