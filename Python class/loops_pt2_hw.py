'''
FOR LOOP HOMEWORK

This homework is meant to test your understanding of WHILE loops. To get started, 

1) Open the folder in which you store all your homework for this class
2) In that folder, create another folder called WhileLoopsHW
    (If you want to create a new folder using the Terminal, type mkdir WhileLoopsHW inside 
    the folder where you store all the homework for this class)
    This file (loops_pt2_hw.py) and autograder.py should be stored in the WhileLoopsHW folder
3) Type all your code in this file
4) Once you finish a function, to test it, type 
    python3 autograder.py 
    inside the WhileLoopsHW folder. This will run the autograder.py file to make sure you are passing
    all the test cases. Alternatively, click on the autograder.py file, select
    Debug -> Run without debugging from the menu bar.
    If you see an assertion failure in the Terminal, then you are 
    NOT passing that given test case. You can look inside the autograder.py file to check 
    which test cases we are using to test your code. You are not done until you pass 
    ALL the test cases!

There are 3 levels in this homework. Please attempt the mild, medium, and spicy problems!
This will allow you to get the most out of this class. The problems increase in difficulty
so start at the top and work your way down. 

Remember to take a look at the attached notesheet about while loops if you are confused
Reach out to us if you are stuck! We want to help!

GOOD LUCK and happy coding
'''

import math

###################
## MILD PROBLEMS ##
###################

def factorial(x):
    '''
    Write a function that returns the value of x factorial

    Ex. factorial(0) --> 1
    Ex. factorial(3) --> 3 * 2 * 1 = 6
    Ex. factorial(5) --> 5 * 4 * 3 * 2 * 1 = 120
    '''
    # YOUR CODE HERE

def numDigits(x):
    '''
    Write a function that counts the number of digits in an int
    Ex. numDigits(134) --> 3
    Ex. numDigits(5) --> 1
    Ex. numDigits(001) --> 1 (ignore leading zeros)
    Ex. numDigits(100) --> 3
    '''
    # YOUR CODE HERE

#####################
## MEDIUM PROBLEMS ##
#####################

def GCF(x, y):
    '''
    Write a function that finds the greatest common factor of x and y
    Ex. GCF(2, 4) --> 2
    Ex. GCF(7, 9) --> 1
    Ex. GCF(24, 32) --> 8
    '''
    # YOUR CODE HERE

#####################
## SPICY PROBLEMS ###
#####################

def nthPrime(n):
    '''
    Write a function that returns the nth prime number
    Ex. nthPrime(1) --> 2   // since 2 is the 1st prime number
    Ex. nthPrime(2) --> 3   // since 3 is the 2nd prime number
    Ex. nthPrime(3) --> 5   // since 5 is the 3rd prime number
    Ex. nthPrime(4) --> 7   // since 7 is the 4th prime number
    Ex. nthPrime(5) --> 11  // since 11 is the 5th prime number

    Hint: use the isPrime(x) function you wrote in last week's homework to help
    you solve this problem
    '''
    # YOUR CODE HERE

def nthFibonacci(n):
    '''
    Write a function that returns the nth Fibonacci number
    Recall the Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13...
    The definition of the Fibonacci series is one in which each number is the sum of the 
    two preceding numbers
    So we start with 1, 1
    Then, we have 
    1+1 = 2
    2+1 = 3
    3+2 = 5
    5+3 = 8
    8+5 = 13 and so on
    Look it up on Google if you're still confused

    Ex. nthFibonacci(1) --> 1
    Ex. nthFibonacci(2) --> 1
    Ex. nthFibonacci(3) --> 2
    Ex. nthFibonacci(4) --> 3
    Ex. nthFibonacci(5) --> 5
    '''
    # YOUR CODE HERE
