# getting ascii which can be useful for alphabetical order
ord('k')

# counting the number of certain item in a list
list_x.count(item)

# The Python set update() method updates the set, adding items from other iterables
A.update(iterable)
A.update(iter1, iter2, iter3)

# The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user
dictionary.fromkeys(sequence[, value])
keys = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(keys)
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)

# getting the index of an element in a list
list_name.index(element)

# poping an element from the end of a list
list_.pop()

# convert labels to ints if their type is bool
if y.dtype == bool:
    y = y.astype(int)
    
# insert an item anywhere in a python list
path.insert(list_position_to_insert_in, whatever_input_you_wish)

# take multiple inputs at once (any of the following codes)
friend_heights = list(map(int, input().split()))
# using list comprehension
friend_heights = [*map(int, input().split())]

# save to a disk
import cPickle as pickle
pickle.dump(dup_cols, open('dup_cols.p', 'w'), protocol=pickle.HIGHEST_PROTOCOL)
friend_heights = [int(x) for idx, x in enumerate(input().split()) if idx < number_of_accepted_inputs]

"""sort by index or by another array"""
# method 1
s = [2, 3, 1, 4, 5, 3]
sorted(range(len(s)), key=lambda k: s[k])
# [2, 0, 1, 5, 3, 4]

# method 2
import numpy
vals = numpy.array([2,3,1,4,5])
vals
array([2, 3, 1, 4, 5])
sort_index = numpy.argsort(vals)
# array([2, 0, 1, 3, 4])

# method 3
vals = [2,3,1,4,5]
sorted(range(len(vals)), key=vals.__getitem__)
# [2, 0, 1, 3, 4]

"""for debugging"""
from IPython.core.debugger import set_trace
# set your breakpoint where you want (put as many as you want)
set_trace()
""" 
Then use:
1. n for next (like step over) don't enter the function
2. s for step (like step into) enters the function
3. c for continue (continue to the next breakpoint) 
while debugging you can print any variable or data structure in your code scope
(i.e. defined in your code scope)
"""

# shortcut for if else
print("one") if condition == 1 else print("else")
# getting the number of lowercase letters in a word
sum(map(str.islower, word))

# useful
print("YNEOS"[any(map(sum, zip(*[map(int, input().split()) for i in ' '*int(input())])))::2])

# input mapping function-like object
inputs = lambda: list(map(int, input().split()))
# then use this
any_current_input,  = inputs()
# or if your inputs are two items use this
x, y = inputs()
