# loop through elements and make a dictionary

keys = ( 'a', 'b', 'c', 'd', 'e', 'f' )
values = ( 0, 1, 2, 3, 4 )

dictionary = dict()
index = 0
for key in keys:
    if index >= len(values):
        break 
    dictionary[key] = values[index] 
    index += 1 # 7 lines
    
print(dictionary) # fixed!  (but ugly)



