import math

def answer(n):
    #n index, go to index + 5
    primeStr = ""
    primeCounter = 0
    i = 2
    keepGoing = True
    while keepGoing:
        isPrime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                #not prime
                isPrime = False
        if isPrime:
            if primeCounter >= n and primeCounter < n + 5:
                primeStr += str(i)
            if primeCounter > n + 4:
                keepGoing = False
            primeCounter += 1
        i += 1
    return primeStr[:5]

print(answer(10000))