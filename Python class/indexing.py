'''
Summary:

1) List Indexing
2) String Indexing
'''

############################
####### LIST INDEXING ######
############################

l = [1, 2, 3, 4]
# l[0] --> 1
# l[1] --> 2
# l[2] --> 3
l[2] = 10
print(l) # [1, 2, 10, 4]

# How do I get the third element of this list? lst[2]
# How do I set it to 5? lst[2] = 5
lst = [4, 2, 3, 1]

# How many elements are in the list?
len(lst)

# TODO: Write a function called findLast that returns the last element of a list
def findLast(lst):
    return lst[len(lst) - 1]

# We can also access the elements of a list via negative indexing!
lst = [90, 3, 56, 4]
# lst[-1] = 4
# lst[-2] = 56
# lst[-3] = 3

# What are two ways to access the first element of a list? P
# Positive indexing: l[0] 
# Negative indexing: l[-1 * len(l)]
l = ["abc", "de", "j"]

# TODO: Write a function that multiplies the first two elements in a list and returns the result 
def multiplies(lst):
    return lst[1] * lst[0]

############################
##### STRING INDEXING ######
############################

# We can also index into strings the same way we can index into a list (they're both collections). Can we index into ints?
s = "snacc attacc"
# s[0] = "s"
# s[1] = "n"
# s[2] = "a"
# s[-1] = "c"
# s[-2] = "c"

# We can find the length of a string
len("ahana") = 5 

# TODO: return the element in the middle of a string
# Ex. "abcde" -> "c"
# Ex. "abcd" -> "b"

def findMiddle(s):
    if len(s) % 2 == 0:
        return s[len(s) / 2 - 1]
    else:
        return s[len(s) // 2]













































"--------------------------------------"

# Correct implementation
def swap(i, j, lst):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst

def swap_main():
    l = [1, 5, 2, 8]
    new_lst = swap(0, len(l) - 1, l)
    print(new_lst)







