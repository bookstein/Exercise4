
"""
My version of list operations exercise,
completed on Friday 10/3 on my own
for practice.

Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list[1:]

def last(input_list):
    """Return the last element of the input list."""
    return input_list[-1]

def init(input_list):
    """Return all elements of the input list except the last."""
    return input_list[:-1]

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list[:3]
    #need to practice knowing that :3 will return 0,1,2 (first three)
    # come back to this one

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list[-5:]

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two.
    """
    return input_list[2:-2]
    # [2:] != 0, 1, 2
    # [2:] --> 0, 1 (first two)
    # come back to this one

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list[2:6]

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return input_list[-6:-2]

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0] = 42

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    input_list[2], input_list[-1] = 37, 37
    # do not put 37 in brackets -- that would add a list inside a list
    # is there a shorter/better way to do this?

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """
    input_list[2:-2] = [42, 37]

def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[6]
    del input_list[2]
    # is there a way to do this where I can put [2] first?

def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """
    input_list[2:-2] = []
    # why doesn't this create an empty list inside a list?

"""
Now would be a great time to ask for a code review.
"""

"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 and 2 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    count = 0
    for item in input_list:
        count += 1
    return count

# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
    #starts with last element, and yet doesn't replace it?
    input_list[custom_len(input_list):] = [value]

    # input_list[-1:] = [value] FAILED
    # this is wrong because it replaced last elem
    # why aren't these two the same?

    # can only assign an iterable to a slice apparently.
    # but only for slices?
    # ie, I can assign list[3] = 44 no prob

def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
    input_list[custom_len(input_list):] = values
    # assume values is a list itself

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    input_list[index:index] = [value]

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
    # remove FIRST matching value, does not return a value
    for index in range(custom_len(input_list)):
        if input_list[index] == value:
            del input_list[index]
            break
    # come back to this one! it took a long time
    # del removes an item from a list given its INDEX not its value
    # this errors without the break line -- causes index out of range

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    pop = input_list[-1]
    del input_list[-1]
    return pop

    # taking a long time. come back to this one!!
    # what the heck?? nothing else that I tried worked.
    # what finally made it work?

    # FAIL: custom_remove(input_list, input_list[custom_len(input_list)])

def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    for index in range(custom_len(input_list)):
        if input_list[index] == value:
            return index

def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""
    count = 0
    for item in input_list:
        if item == value:
            count += 1
    return count

def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""
    for i in range(custom_len(input_list)/2):
        temp = input_list[i]
        input_list[i] = input_list[-1-i]
        input_list[-1-i] = temp

def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    for item in input_list:
        if item == value:
            return True
            break

def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    if custom_len(some_list) == custom_len(another_list):
        for index in range(custom_len(another_list)): # for loop by length of list
            if some_list[index] == another_list[index]: # checks equality
                return True

    else:
        return False # returns true after checking all values


    # come back to this one too -- taking a looooong time



