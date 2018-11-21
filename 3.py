# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math


def get_largest_prime_factor(n):
    primes = []
    if n <= 2:
        raise ValueError("n must be greater than 2")

    largest_prime_factor = 2
    for i in range(2, int(math.sqrt(n))):
        skip = False
        for prime in primes:
            # numbers are divisible only up to their square roots
            if prime > math.sqrt(i):
                break
            if i % prime == 0:
                skip = True
                break
        if skip:
            continue
        primes.append(i)
        if n % i == 0:
            largest_prime_factor = i
    return largest_prime_factor


print(get_largest_prime_factor(600851475143))

