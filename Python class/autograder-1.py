from loops_pt2_hw import factorial, numDigits, GCF, nthPrime, nthFibonacci

def testFactorial():
    assert(factorial(0) == 1)
    assert(factorial(1) == 1)
    assert(factorial(2) == 2)
    assert(factorial(3) == 6)
    assert(factorial(4) == 24)
    assert(factorial(5) == 120)
    assert(factorial(6) == 720)
    assert(factorial(15) == 1307674368000)

def testNumDigits():
    assert(numDigits(134) == 3)
    assert(numDigits(5) == 1)
    assert(numDigits(1) == 1)
    assert(numDigits(100) == 3)

def testGCF():
    assert(GCF(2, 4) == 2)
    assert(GCF(7, 9) == 1)
    assert(GCF(24, 32) == 8)
    assert(GCF(100, 150) == 50)
    assert(GCF(24, 24) == 24)
    assert(GCF(28, 52) == 4)
    assert(GCF(36, 108) == 36)

def testNthPrime():
    assert(nthPrime(1) == 2)
    assert(nthPrime(2) == 3)
    assert(nthPrime(3) == 5)
    assert(nthPrime(4) == 7)
    assert(nthPrime(5) == 11)

def testNthFibonacci():
    assert(nthFibonacci(1) == 1)
    assert(nthFibonacci(2) == 1)
    assert(nthFibonacci(3) == 2)
    assert(nthFibonacci(4) == 3)
    assert(nthFibonacci(5) == 5)

if __name__ == "__main__":
    print()
    print("Running the autograder: ")
    print("-------------------")
    testFactorial()
    print("PASSED ALL TESTS FOR FACTORIAL")
    print("Score: 1/5")
    print("-------------------")
    testNumDigits()
    print("PASSED ALL TESTS FOR NUM DIGITS")
    print("Score: 2/5")
    print("-------------------")
    testGCF()
    print("PASSED ALL TESTS FOR GCF")
    print("Score: 3/5")
    print("-------------------")
    testNthPrime()
    print("PASSED ALL TESTS FOR NTH PRIME")
    print("Score: 4/5")
    print("-------------------")
    testNthFibonacci()
    print("PASSED ALL TESTS FOR NTH FIBONACCI")
    print("Score: 5/5")
    print("-------------------")