# loop through elements and make a dictionary

keys = ( 'a', 'b', 'c', 'd', 'e', 'f' )
values = ( 0, 1, 2, 3, 4 )

if len(keys) > len(values):
    value_mode = True
else:
    value_mode = False
    
if value_mode:
    enumerate_me = values
else:
    enumerate_me = keys

dictionary = dict() # wayy too many lines
for index, value_or_key in enumerate(enumerate_me):
    if value_mode:
        dictionary[keys[index]] = value_or_key
    else:
        dictionary[value_or_key] = values[index]
    
print(dictionary) # Works, but now you're just making me mad



