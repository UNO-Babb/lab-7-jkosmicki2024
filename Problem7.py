#Problem 7 - 10001st prime 
def main():
    from NumberTests import isPrime
    
    def numPrimes(n):
        numberofPrimes = 0
        prime = 1
        while numberofPrimes < n:
            prime += 1
            if isPrime(prime):
                numberofPrimes += 1
        return prime
    
    print(numPrimes(10001)) 
if __name__ == '__main__':
    main()