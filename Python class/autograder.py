from loops_hw import numOdds, listSum, isPrime, isSorted, reverseLstNeg, reverseLstPos

lst_1 = [1, 3, 4]
lst_2 = []
lst_3 = [2, 4, 6, 8]
lst_4 = [1, 3, 5]
lst_5 = [0, 1, 2, 0, 1]
lst_6 = [-1, 2, -1]
lst_7 = [1, 2, 2, 2]

def gradeNumOdds():
    assert(numOdds(lst_1) == 2)
    assert(numOdds(lst_2) == 0)
    assert(numOdds(lst_3) == 0)
    assert(numOdds(lst_4) == 3)
    assert(numOdds(lst_5) == 2)
    assert(numOdds(lst_6) == 2)

def gradeListSum():
    assert(listSum(lst_1) == 8)
    assert(listSum(lst_2) == 0)
    assert(listSum(lst_3) == 20)
    assert(listSum(lst_4) == 9)
    assert(listSum(lst_5) == 4)
    assert(listSum(lst_6) == 0)

def gradeIsPrime():
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

def gradeIsSorted():
    assert(isSorted(lst_1) == True)
    assert(isSorted(lst_2) == True)
    assert(isSorted(lst_3) == True)
    assert(isSorted(lst_4) == True)
    assert(isSorted(lst_5) == False)
    assert(isSorted(lst_6) == False)
    assert(isSorted(lst_7) == True)

def gradeReverseLstNeg():
    assert(reverseLstNeg(lst_1) == [4, 3, 1])
    assert(reverseLstNeg(lst_2) == [])
    assert(reverseLstNeg(lst_3) == [8, 6, 4, 2])
    assert(reverseLstNeg(lst_4) == [5, 3, 1])
    assert(reverseLstNeg(lst_5) == [1, 0, 2, 1, 0])
    assert(reverseLstNeg(lst_6) == [-1, 2, -1])
    assert(reverseLstNeg(lst_7) == [2, 2, 2, 1])

def gradeReverseLstPos():
    assert(reverseLstPos(lst_1) == [4, 3, 1])
    assert(reverseLstPos(lst_2) == [])
    assert(reverseLstPos(lst_3) == [8, 6, 4, 2])
    assert(reverseLstPos(lst_4) == [5, 3, 1])
    assert(reverseLstPos(lst_5) == [1, 0, 2, 1, 0])
    assert(reverseLstPos(lst_6) == [-1, 2, -1])
    assert(reverseLstPos(lst_7) == [2, 2, 2, 1])

if __name__ == "__main__":
    print("Running the autograder: ")
    print("-------------------")
    gradeNumOdds()
    print("PASSED ALL TESTS FOR NUM ODDS")
    print("Score: 1/6")
    print("-------------------")
    gradeListSum()
    print("PASSED ALL TESTS FOR LIST SUM")
    print("Score: 2/6")
    print("-------------------")
    gradeIsPrime()
    print("PASSED ALL TESTS FOR IS PRIME")
    print("Score: 3/6")
    print("-------------------")
    gradeIsSorted()
    print("PASSED ALL TESTS FOR IS SORTED")
    print("Score: 4/6")
    print("-------------------")
    gradeReverseLstNeg()
    print("PASSED ALL TESTS FOR REVERSED LIST USING NEGATIVE INDEXING")
    print("Score: 5/6")
    print("-------------------")
    gradeReverseLstPos()
    print("PASSED ALL TESTS FOR REVERSED LIST USING POSITIVE INDEXING")
    print("Score: 6/6")
    print("-------------------")