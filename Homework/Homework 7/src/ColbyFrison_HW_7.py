# Name: Colby Frison
# OUID: 113568816
# Date: 4/21/2025
# Class: CS3323
# Assignment: Homework 7
# Description: This program implements generators to find SuPrP2(sum of prime and power of 2) numbers

# is prime function
def isPrime(n):
    """
    Similar to the isPrime function from class, but with some additional
    optimizations, like using the property that all primes greater than 
    3 are of the form 6k +/- 1 to reduce the number of checks.
    
    Args:
        n (int): num to check if prime
    
    Returns:
        bool: True if the num is prime, False otherwise
    """
    # First check the base case and small primes
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility using 6k +- 1 optimization
    # This is more efficient than checking all numbers up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    # If no divisors found, n is prime
    return True


# power of two generator
def powerOfTwoGenerator():
    """
    Generator that yields all powers of two starting from 2^0
    
    This is pretty much just the function from class, but in 
    class it was called lazySq()
    
    Yields:
        int: The next power of 2 in the sequence
    """
    # Start with exponent 0 (2^0 = 1)
    exponent = 0
    
    # Yield powers of 2 indefinitely
    while True:
        yield 2 ** exponent
        exponent += 1


# SuPrP2 num generator
def suprp2Generator(n):
    """
    Generator that yields all SuPrP2 numbers greater than n in increasing order.
    
    A SuPrP2 num is an integer that can be written as the sum of a prime and
    a power of 2. This generator follows the pattern from our class notes on
    creating generators that filter values based on a condition.
    
    Args:
        n (int or str): The starting num
    
    Yields:
        tuple: (suprp2Number, primeComponent, powerOfTwo, powerExponent)

    I could just return the number, but I have it returning the tuple so I can have the output with the components
    """
    # Make sure n is an int
    n = int(n)
    
    # Create a list to store powers of 2
    powersOfTwo = []

    # Create the generator for powers of 2
    powerGen = powerOfTwoGenerator()
    
    # Start checking numbers after n
    currentNum = n + 1
    
    # Create a hashmap for caching prime check results
    # This prevents re-checking the same num to see if prime
    # and considering the size of numbers we are checking, its 
    # kind of a necessary addition
    primeCache = {}
    
    # Keep generating SuPrP2 numbers indefinitely
    while True:
        # Initialize variables for the current num
        isSuPrP2 = False # bool to check if the current num is a SuPrP2
        prime = None # prime component
        power = None # power of two component
        exponent = None # exponent of the power of two
        
        # Ensure we have enough powers of 2 to check
        while len(powersOfTwo) == 0 or powersOfTwo[-1] < currentNum:
            powersOfTwo.append(next(powerGen))
        
        # Check if current num can be expressed as prime + power of 2
        for idx, power in enumerate(powersOfTwo):
            # Skip powers that are too large
            if power >= currentNum:
                break
            
            # Check if (current - power) is prime
            potentialPrime = currentNum - power
            
            # if num were checking isn't in the cache, check if its prime
            if potentialPrime not in primeCache:
                primeCache[potentialPrime] = isPrime(potentialPrime)
            
            # refresh the cache to see if the num is prime
            if primeCache[potentialPrime]:
                # Found a valid decomposition
                isSuPrP2 = True
                prime = potentialPrime
                power = power
                exponent = idx
                break
        
        # Yield the SuPrP2 num and its components if found
        if isSuPrP2:
            # 4-tuple of the SuPrP2 num, the prime component, the power of two, and the exponent
            # This makes the output look nice and explains the components of the SuPrP2 num
            yield (currentNum, prime, power, exponent)
        
        # Move to the next num
        currentNum += 1


#  Main section 

# my student ID
ID = "113568816"

# 1. Powers of two generator
print("\nProblem 1: Powers of Two Generator")
print("First few powers of two:")
p2Gen = powerOfTwoGenerator()
for i in range(5):
    print(f"2^{i} = {next(p2Gen)}")

# 2. SuPrP2 num generator
print("\nProblem 2: SuPrP2 Numbers Generator")
print("First few SuPrP2 numbers greater than 10:")
sp2Gen = suprp2Generator(10)
for i in range(5):
    result = next(sp2Gen)
    print(f"{result[0]} = {result[1]} + 2^{result[3]} (prime + {result[2]})")


# 3. SuPrP2 gen but 20 after student ID
print("\nProblem 3: 20 SuPrP2 Numbers After Student ID")

# Use our generator to find the SuPrP2 numbers
sp2Gen = suprp2Generator(ID)
results = []

# Collect 20 SuPrP2 numbers
for _ in range(20):
    result = next(sp2Gen)
    results.append(result)
    suprp2, prime, power, exponent = result
    print(f"{suprp2} = {prime} + 2^{exponent} (prime + {power})")



# Results for question 3 - adding these as comments in the source code
"""
113568819 = 113568787 + 2^5 (prime + 32)
113568821 = 46459957 + 2^26 (prime + 67108864)
113568823 = 113568311 + 2^9 (prime + 512)
113568825 = 113536057 + 2^15 (prime + 32768)
113568827 = 113568571 + 2^8 (prime + 256)
113568829 = 113536061 + 2^15 (prime + 32768)
113568831 = 113560639 + 2^13 (prime + 8192)
113568833 = 113568769 + 2^6 (prime + 64)
113568835 = 111471683 + 2^21 (prime + 2097152)
113568837 = 113568773 + 2^6 (prime + 64)
113568840 = 113568839 + 2^0 (prime + 1)
113568841 = 113568839 + 2^1 (prime + 2)
113568843 = 113568839 + 2^2 (prime + 4)
113568845 = 46459981 + 2^26 (prime + 67108864)
113568847 = 113568839 + 2^3 (prime + 8)
113568849 = 113564753 + 2^12 (prime + 4096)
113568851 = 113568787 + 2^6 (prime + 64)
113568853 = 113560661 + 2^13 (prime + 8192)
113568854 = 113568853 + 2^0 (prime + 1)
113568855 = 113568853 + 2^1 (prime + 2)
"""
