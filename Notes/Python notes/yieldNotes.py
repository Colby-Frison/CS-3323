# The 'yield' keyword in Python is used to create generator functions. 
# Unlike regular functions that return a single value and terminate, 
# generator functions can yield multiple values over time, pausing 
# their execution and preserving their state between each yield. 
# This allows for memory-efficient iteration over large datasets, 
# as values are generated one at a time rather than all at once.

# values are generated one at a time rather than all at once.
def myList():
    yield 1  # Pauses here, returns 1, resumes on next call
    yield 2  # Pauses here, returns 2, resumes on next call
    yield "OU"  # Pauses here, returns "OU", resumes on next call

# Iterate through each value yielded by the generator
# For each value, multiply it by 2 and print the result
# Numbers will be multiplied, strings will be repeated
for x in myList():
    print(x*2)

print("###################################################")

# Define a generator function that yields square numbers
def lazysq():
    i = 0  # Initialize counter
    while (True):  # Infinite loop to keep generating squares
        yield i*i  # Yield the square of current number
        i = i + 1  # Increment counter for next square

# Use the generator to print squares until we exceed 100
for x in lazysq():  # Get next square from generator
    if x > 100:     # Stop when we reach a square greater than 100
        break
    print(x)        # Print the current square

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# example usage
print("\nExample usage of is prime: ")
print("11 is prime: ", is_prime(11))
print("15 is prime: ", is_prime(15))
print("2 is prime: ", is_prime(2))
print("1 is prime: ", is_prime(1))

def lazy_prime():
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 1

print("\nprime numbers from 2 to 1000: ")
for p in lazy_prime():
    if p > 1000:
        break
    print(p)

# twin prime
print("twin primes from 1 - 100: ", [x for x in range(100) if is_prime(x) and is_prime(x+2)])

def is_nice(n):
    # anumber n iss nice if it is a sim of a prime and a square
    for i in lazy_prime():
        if i > n:
            return False
        if is_prime(n - i):
            return True

print("\nNice numbers from 1 - 100: ", [x for x in range(100) if is_nice(x)])

print("###################################################")

# Pure functional factorial in python
# Pure functional means no loops, only recursion
def pffac(n):
    if n == 0:
        return 1
    else:
        return pffac(n - 1)*n

print("\nPure functional factorial: ", pffac(5))

# binary search for integer approximation of the root
# f(lower) <= a and f(upper) >= a
def root_f(f, a, lower, upper):
    if lower >= upper - 1:
        if f(upper) == a:
            return upper
        else:
            return lower
    mid = (lower + upper) // 2
    if f(mid) >= a:
        return root_f(f, a, lower, mid)
    else:
        return root_f(f, a, mid, upper)


print("\nRoot of f(x) = x^2 - 2: ", root_f(lambda x: x*x, 81, 0, 100))
