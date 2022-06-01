## Find Even Numbers
## Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.

def evens(lst):
    return [ x for x in lst if x % 2 == 0]
print(evens([2, 7, 10, 11, 12])) 