# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

min_product = 100 * 100
max_product = 999 * 999

largest_palindrome = -1
for i in range(999, 100, -1):
    for j in range(999, i, -1):
        product = i * j
        n = product
        reverse_n = 0
        # trailing 0s can never be part of a palindrome because there are no leading 0s
        if n % 10 == 0:
            continue
        while n > 0:
            digit = n % 10
            reverse_n *= 10
            reverse_n += digit
            n //= 10

        if reverse_n == product and product > largest_palindrome:
            largest_palindrome = product
            break

print(largest_palindrome)





