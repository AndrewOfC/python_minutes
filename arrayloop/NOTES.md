
# Description

There's 
a right way
a wrong way
and a Pythonic way



(I don't care what the OCDs at the OED say, "Pythonic" is a word.)

Please like, share, subscribe and if there's something about python you want to learn condensed in a minute, leave a comment.

# Script

## array1.py

When you've come out of the C/C++ world, this might be your first cut at iterating over an array.
While this is not wrong, there are better ways to do it.

## array2.py

We see a slight improvement here. (* highlight the 'in strings' *) At least we're making use of the for loop's facility for iterating an array 

## array3.py

If you need to have the indices of the elements you're iterating over, this is the most pythonic way of doing it.  (* highlight i,s *) Note the python for-loops have the capacity to manage multiple variables 

(* highlight enumerate *) enumerate is a builtin function that produces a 'generator' that yields index,element pairs.  Each pass in the for-loop will have i set to the index in the array and s set to the element