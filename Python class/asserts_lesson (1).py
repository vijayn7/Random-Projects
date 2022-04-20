#########################
### FUNCTIONS REVIEW ####
#########################

# Code Tracing
z = 5 # global variable

def f(x, y):
    if (x % 2) == 0:
        print("baby", x)
        return x + 4, z
    else:
        print("man", x)

    if False:
        print("no way")

    return x + 3, z

def g(z):
    print("boss")
    z = z + 3
    return z

# a = g(3)      // 1) What does this print? boss     2) what is the value of a? 6
# print(a)      // a = 6
# b = f(6,4)    // 1) What does this print? baby 6    2) what is the value of b? (10, 5)
# print(b)      // (10, 5)
# c = g(b[0])   // b[0] = 10, g(10) prints boss and c = 13
# print(c)      // 13

# How would you write c in one line?
# g(f(g(3), 4)[0])

#--------------------------------------------------------

# TODO: Write a function that takes in 2 inputs: an int and the place in the int we want to find
# findDigit(123, 2) = 1
# findDigits(123, 0) 3
# findDigits(123, 1) = 2
# 0 -> ones place
# 1 -> tens place 
# 2 -> hundreds place
# 
# can index into:
# - list
# - strings
# - tuples
str(123) -> "123"
int(34.5) -> 34
float(34) -> 34.0
bool(5) -> True

def findDigit(n, k):
    str_n = str(n)
    if k < 0:
        return None
    if k >= len(str_n):
        return 0
    return str_n[len(str_n) - k - 1]


#########################
### TESTING YOUR CODE ###
#########################

def isEven(x):
    return (x % 2) == 0

'''
Let's supposed we have written a function that is supposed to return true if a numbers is even
and false otherwise
How do we know it works? We have to test it. What exactly are we testing?

To test, we use assert statements in Python
assert is a function that takes in one argument: a boolean
If the boolean is True, it doesn't do anything
If the boolean is False, it raises an AssertionError
'''

# assert(1 == 1) # True so does nothing
# assert(1 == 2) # False so raises an assertion error

# TODO: how do we test the function isEven
assert(isEven(10) == True)
assert(isEven(4) == True)
assert(isEven(5) == False)
assert(isEven(0) == True)
assert(isEven(-12) == True)
assert(isEven(-11) == False)

# TODO: how do we test the function isPrime(x) which takes in one argument and is supposed to return True 
# if a number is prime and false otherwise

def testFn(isPrime):
    '''
    We need to grade the homework of 9 students who all wrote an incorrect isPrime function
    As teachers, we need to write assert statements that will cause their code to fail
    Currently, their broken implementations are passing our tests because we have no tests!
    '''
    assert(isPrime(1) == False)
    assert(isPrime(-1) == False)
    assert(isPrime(2) == True)
    assert(isPrime(-3) == False)
    assert(isPrime(-2) == False)
    assert(isPrime(0) == False)
    assert(isPrime(3) == True)
    assert(isPrime(212) == False)
    assert(isPrime(213) == False)
    assert(isPrime(4) == False)
    assert(isPrime(1.1) == False)
    assert(isPrime(-3.2) == False)
    assert(isPrime(True) == False)
    assert(isPrime(False) == False)
    assert(isPrime("3") == False)
    assert(isPrime("abcd") == False)






