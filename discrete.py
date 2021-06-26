"""
    Experiments in the form of step-by-step tests to demonstrate some attempted self-implemented algorithms to perform discrete-mathematical calculations, by coded computational means.
    
    This is a personal test to see whether I: (a) adequately understand some of the concepts; and (b) can use and demonstrate programming knowledge by putting the concepts into practical-computational use.
    @author: Nathaniel Schmidt<schmidty2244@gmail.com>
"""

from math import sqrt, floor# <https://docs.python.org/3/library/math.html>

# Number Theory:
def divides (a, b):
    """
        Determines whether positive int $b$ can be divided by whole number $a$ without remainders.
        @param a: the first int.
        @type a: int
        @param b: the second int.
        @type b: int
        @returns: The resulting truth value of the conditionally-tested input parameters.
        @rtype: bool
    """
    
    return b%a == 0

def readDivides ():
    a = int (input ("Enter the divisor"))
    b = int (input ("Enter the number to be divided"))
    return divides (a, b)

def readDividesTest ():
    if readDivides ():
        print ("Yes, this divides")
    else:
        print ("No, this does not divide without remainders")

# test, do this twice to test alternative results
readDividesTest ()
readDividesTest ()

def isPrime (num):
    """
        Taken and modified from <https://www.programiz.com/python-programming/examples/prime-number>
    """
    
    if num > 1:
        for i in range (2, num):
            if num%i == 0:
                return False
                break
            else:
                return True

def readPrime ():
    num = int(input("Enter a number"))
    while num < 2:
        print ("Please enter at least a positive number greater than one")
        num = int(input("Enter a prime number"))
    return num

def readPrimeTest ():
    num = readPrime ()
    if isPrime (num):
        print ("This is a prime number")
    else:
        print ("this is not a prime number")

# Test
readPrimeTest ()
readPrimeTest ()

def findPrimes (num):
    """
        this is the first practical step in determining the prime factorisations for any given positive int.  We want to find (and start factorising from) the prime number closest to but less than the square root of the number we are wanting to prime-factorise, then return the primes to be tested.
        
        NOTE: more robust working algorithm at https://stackoverflow.com/questions/15347174/python-finding-prime-factors
    """
    
    primes = []
    maxTest = sqrt(num)
    
    if not maxTest.is_integer ():
        maxTest = floor(maxTest)# Built-in floor quotient operator doesn't always convert from float to int, so use function from std. lib.
    
    for i in range(2, maxTest):
        if isPrime (i):
            primes.append (i)
        else:
            continue
    
    primes = primes.reverse ()
    return primes

def readTestedPrimes ():
    num = int (input ("Enter the number to find testable primes for"))
    primes = findPrimes (num)
    return primes

def printPrimes ():
    primes = readTestedPrimes ()
    print(primes)

printPrimes ()
