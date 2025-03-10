#Problem 10 - Summation of primes
from NumberTests import isPrime
def sumofPrimes(summation):
    total = 0
    for n in range(2, summation):
        if isPrime(n):
            total += n
    return total
def main():
    result = sumofPrimes(2000000)
    print(result)
if __name__== "__main__":
    main()