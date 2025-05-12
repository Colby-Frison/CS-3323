# question 1

# Use recursion in Python to write a program that given a positive integer n, calculates the sum of the
# first n integer squares. So

# sofsq(1) = 1*1 = 1
# sofsq(2) = 1*1 + 2*2 = 5
# sofsq(3) = 1*1 + 2*2 + 3*3 = 14

def sofsq(n):
    if n == 1:
        return 1
    else:
        return n*n + sofsq(n-1)

print(sofsq(1))
print(sofsq(2))
print(sofsq(3))
print(sofsq(4))


# Question 2
# Use yield to write a Python generator sofcu that produces all the sums of consecutive integer cubes. The first
# three sofcu are
# 1 (= 1*1*1), 9(= 1*1*1+2*2*2), 36 (= 1*1*1+2*2*2+3*3*3)
# You should write only one function ( generator ), i.e. you should not use helper functions.

def sofcu():
    i = 1
    total = 0
    while True:
        total += i * i * i
        yield total
        i += 1

gen = sofcu()

for i in range(3):
    print(next(gen))
