# loop through elements and make a dictionary

keys = ( 'a', 'b', 'c', 'd', 'e', 'f' )
values = ( 0, 1, 2, 3, 4 )

dictionary = dict()
index = 0
for key in keys:
    dictionary[key] = values[index] # oops :(
    index += 1 # 5 lines
    
print(dictionary)



