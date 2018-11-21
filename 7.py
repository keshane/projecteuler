#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?
import math


def nth_prime_number(n):
    primes = []
    i = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime > int(math.sqrt(i)):
                break
            if i % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
        i += 1

    # get last prime
    return primes[-1]


print(nth_prime_number(10001))
