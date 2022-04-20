'''
FOR LOOP HOMEWORK

This homework is meant to test your understanding of for loops. To get started, 

1) Open the folder in which you store all your homework for this class
2) In that folder, create another folder called LoopsHW
    (If you want to create a new folder using the Terminal, type mkdir LoopsHW inside 
    the folder where you store all the homework for this class)
    This file and autograder.py should be stored in the LoopsHW folder
3) Type all your code in this file
4) Once you finish a function, type 
    python3 autograder.py 
    inside the LoopsHW folder. This will run the autograder.py file to make sure you are passing
    all the test cases. Alternatively, click on the autograder.py file, select
    Debug -> Run without debugging from the menu bar.
    If you see an assertion failure in the Terminal, then you are 
    NOT passing that given test case. You can look inside the autograder.py file to check 
    which test cases we are using to test your code. You are not done until you pass 
    ALL the test cases!

There are 3 levels in this homework. Please attempt the mild, medium, and spicy problems!
This will allow you to get the most out of this class. The problems increase in difficulty
so start at the top and work your way down. 

Remember to take a look at the attached notesheet about for loops if you are confused
Reach out to us if you are stuck! We want to help!

GOOD LUCK and happy coding
'''

import math

###################
## MILD PROBLEMS ##
###################

def numOdds(l):
    '''
    Write a function that returns the number of odd numbers in a list
    Ex. numOdds([1, 2, 3]) --> 2
    '''
    # YOUR CODE HERE


def listSum(l):
    '''
    Write a function that returns the sum of the numbers in a list
    Ex. listSum([1, 2, 3]) --> 6
    '''
    # YOUR CODE HERE


#####################
## MEDIUM PROBLEMS ##
#####################

def isPrime(n):
    '''
    Write a function that returns True if a number is prime and False otherwise
    Think about edge cases! We will be testing this function using the test cases
    you wrote in class.
    '''
    # YOUR CODE HERE


def isSorted(lst):
    '''
    Write a function that returns True if the input list is sorted in non-decreasing order and 
    False otherwise
    Ex. isSorted([1, 2, 3, 4]) --> True
    Ex. isSorted([1, 1, 2, 2]) --> True
    Ex. isSorted([1, 2, 1, 3]) --> False
    '''
    # YOUR CODE HERE

#####################
## SPICY PROBLEMS ###
#####################

# TODO: Write two function that reverses a list
# Ex. reverseLst([1, 2, 3]) --> [3, 2, 1]
# Ex. reverseLst([2, 2, 2]) --> [2, 2, 2]
# Do NOT use the builtin python function reverse()
# As a challenge, write this function in the following 2 ways:
#   1) a for loop with negative increments
#   2) a for loop with positive increments
# Hint: you may want to use the append function to add elements to a list
# Ex. lst = []
# lst.append(1) 
# print(lst) # This will print [1]

def reverseLstNeg(lst):
    '''
    Write a function that reverses a list using a for loop with NEGATIVE increments
    The output of this function should be the reversed list
    Remember the increment is specified in the third argument of the range function:
        range(start, end, increment)
    Check the attached for loop notesheet for additional help
    '''
    # YOUR CODE HERE

def reverseLstPos(lst):
    '''
    Write a function that reverses a list using a for loop with POSITIVE increments
    The output of this function should be the reversed list
    Remember the increment is specified in the third argument of the range function:
        range(start, end, increment)
    Check the attached for loop notesheet for additional help
    '''
    # YOUR CODE HERE
