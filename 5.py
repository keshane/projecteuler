# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def get_lcm_up_to(n):
    if n == 2:
        return 2
    if n < 2:
        raise ValueError("Input must be greater than 1")

    lcm_prime_factors = [2]
    lcm = 2
    for i in range(3, n + 1):
        for prime_factor in lcm_prime_factors:
            if i % prime_factor == 0:
                i //= prime_factor
        if i != 1:
            lcm_prime_factors.append(i)
            lcm *= i

    return lcm

print(get_lcm_up_to(20))

