#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
#
import math


def sum_of_primes_below(n):
    primes = []
    sum_primes = 0
    i = 2
    while i < n:
        is_prime = True
        for prime in primes:
            if prime > int(math.sqrt(i)):
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            sum_primes += i

        # only check odd numbers
        if i > 2:
            i += 2
        else:
            i += 1

    return sum_primes


print(sum_of_primes_below(2000000))




