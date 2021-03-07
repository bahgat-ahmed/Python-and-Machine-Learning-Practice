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
