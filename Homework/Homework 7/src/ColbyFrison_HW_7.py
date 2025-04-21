"""
Name: Colby Frison
OUID: 113568816
Date: 4/21/2025
Class: CS3323
Assignment: Homework 7

This program implements generators to find SuPrP2 numbers - integers that can be 
written as a sum of a prime and a power of 2.
"""

# ===== Section handling the is_prime functions =====

def isPrime(n):
    """
    This is the same is_prime function from class
    It does exactly what it says it does, checks if a number is prime.
    
    Args:
        n (int): The number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """

    # First check the base case
    if n <= 1:
        return False
    
    # Start checking divisibility from i=2
    i = 2
    
    # Only need to check up to square root of n
    while i * i <= n:
        # If n is divisible by any number, it's not prime
        if n % i == 0:
            return False
        # Check the next number
        i += 1
    
    # If no divisors found, n is prime
    return True


# ===== Section handling the power of two generator =====

def powerOfTwoGenerator():
    """
    Generator that yields all powers of two starting from 2^0
    
    This is once again from class, but in class it was called lazySq()
    
    Yields:
        int: The next power of 2 in the sequence
    """
    # Start with exponent 0 (2^0 = 1)
    exponent = 0
    
    # Yield powers of 2 indefinitely
    while True:
        yield 2 ** exponent
        exponent += 1


# ===== Section handling the SuPrP2 number generator =====

def suprp2Generator(n):
    """
    Generator that yields all SuPrP2 numbers greater than n in increasing order.
    
    A SuPrP2 number is an integer that can be written as the sum of a prime and
    a power of 2. This generator follows the pattern from our class notes on
    creating generators that filter values based on a condition.
    
    Args:
        n (int or str): The starting number (exclusive)
    
    Yields:
        tuple: (suprp2Number, primeComponent, powerOfTwo, powerExponent)
    """
    # Make sure n is an integer for arithmetic operations
    n = int(n)
    
    # Create a list to store powers of 2 (memoization technique)
    powersOfTwo = []
    powerGen = powerOfTwoGenerator()
    
    # Start checking numbers after n
    currentNum = n + 1
    
    # Keep generating SuPrP2 numbers indefinitely
    while True:
        # Initialize variables for the current number
        isSuPrP2 = False
        foundPrime = None
        foundPower = None
        foundExponent = None
        
        # Ensure we have enough powers of 2 to check
        while len(powersOfTwo) == 0 or powersOfTwo[-1] < currentNum:
            powersOfTwo.append(next(powerGen))
        
        # Check if current number can be expressed as prime + power of 2
        for idx, power in enumerate(powersOfTwo):
            # Skip powers that are too large
            if power >= currentNum:
                break
            
            # Check if (current - power) is prime
            potentialPrime = currentNum - power
            if isPrime(potentialPrime):
                # Found a valid decomposition
                isSuPrP2 = True
                foundPrime = potentialPrime
                foundPower = power
                foundExponent = idx
                break
        
        # Yield the SuPrP2 number and its components if found
        if isSuPrP2:
            # 4-tuple of the SuPrP2 number, the prime component, the power of two, and the exponent
            # This makes the output look nice and explains the components of the SuPrP2 number
            yield (currentNum, foundPrime, foundPower, foundExponent)
        
        # Move to the next number
        currentNum += 1


# ===== Section handling the main program and output =====

# random number used for the student ID
studentID = "93802475"

# Demonstrate Problem 1: Generator for powers of two
print("\nPROBLEM 1: Powers of Two Generator")
print("First few powers of two:")
p2Gen = powerOfTwoGenerator()
for i in range(5):
    print(f"2^{i} = {next(p2Gen)}")

# Demonstrate Problem 2: Generator for SuPrP2 numbers
print("\nPROBLEM 2: SuPrP2 Numbers Generator")
print("First few SuPrP2 numbers greater than 10:")
sp2Gen = suprp2Generator(10)
for i in range(5):
    result = next(sp2Gen)
    print(f"{result[0]} = {result[1]} + 2^{result[3]} (prime + {result[2]})")

# Solve Problem 3: Find 20 consecutive SuPrP2 numbers after student ID
print("\nPROBLEM 3: SuPrP2 Numbers After Student ID")
print(f"20 consecutive SuPrP2 numbers right after {studentID}:")

# Use our generator to find the SuPrP2 numbers
sp2Gen = suprp2Generator(studentID)
results = []

# Collect 20 SuPrP2 numbers
for _ in range(20):
    result = next(sp2Gen)
    results.append(result)
    suprp2, prime, power, exponent = result
    print(f"{suprp2} = {prime} + 2^{exponent} (prime + {power})")

# Results for question 3 - adding these as comments in the source code
"""
93802477 = 93802469 + 2^3 (prime + 8)
93802478 = 93802477 + 2^0 (prime + 1)
93802479 = 93802477 + 2^1 (prime + 2)
93802481 = 93802477 + 2^2 (prime + 4)
93802483 = 93794291 + 2^13 (prime + 8192)
93802484 = 93802483 + 2^0 (prime + 1)
93802485 = 93802483 + 2^1 (prime + 2)
93802487 = 93802483 + 2^2 (prime + 4)
93802489 = 93801977 + 2^9 (prime + 512)
93802491 = 93802483 + 2^3 (prime + 8)
93802493 = 93802477 + 2^4 (prime + 16)
93802495 = 93802463 + 2^5 (prime + 32)
93802497 = 93802433 + 2^6 (prime + 64)
93802499 = 93802483 + 2^4 (prime + 16)
93802501 = 93802469 + 2^5 (prime + 32)
93802503 = 93801991 + 2^9 (prime + 512)
93802507 = 93800459 + 2^11 (prime + 2048)
93802509 = 93802477 + 2^5 (prime + 32)
93802511 = 93540367 + 2^18 (prime + 262144)
93802513 = 93671441 + 2^17 (prime + 131072)
"""

