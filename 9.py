# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for c in range(997, 2, -1):
    max_b = 1000 - c - 1
    for b in range(max_b, int(max_b // 2), -1):
        a = 1000 - c - b
        if a**2 + b**2 == c**2:
            print("{0}^2 + {1}^2 = {2}^2".format(a, b, c))
            print(a*b*c)



