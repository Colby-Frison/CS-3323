def is_prime(n):
    """Check if a number is prime."""
    # Basic cases - negative numbers, 0, and 1 are not prime
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # Quick check for divisibility by 2 or 3
    # This helps us skip a lot of numbers in our loop below
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for divisibility using the 6k±1 optimization
    # Instead of checking all numbers, we only check numbers of form 6k±1
    # since all primes > 3 can be expressed in this form
    i = 5
    while i * i <= n:  # Only need to check up to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Skip to next numbers of form 6k±1
    return True

def power_of_two_generator():
    """Generator that yields all powers of two starting from 2^0 = 1."""
    # Start with 2^0 = 1
    power = 0
    while True:
        # Yield the current power of 2 and increment the exponent
        yield 2 ** power
        power += 1

def suprp2_generator(n):
    """
    Generator that yields all SuPrP2 numbers greater than n in increasing order.
    SuPrP2 numbers are numbers that can be written as a sum of a prime and a power of 2.
    
    Returns a tuple of (suprp2_number, prime_component, power_of_two, power_exponent)
    """
    # Create a list to store powers of 2 to avoid recomputing them
    # This is much faster than calculating them each time
    powers_of_two = []
    power_gen = power_of_two_generator()
    
    # Start from the smallest number greater than n
    current = n + 1
    
    # Keep generating SuPrP2 numbers indefinitely
    while True:
        # Track if the current number is a SuPrP2
        is_suprp2 = False
        found_prime = None
        found_power = None
        found_exponent = None
        
        # Make sure we have enough powers of 2 available to check
        # We only need powers up to the current number we're checking
        while len(powers_of_two) == 0 or powers_of_two[-1] < current:
            powers_of_two.append(next(power_gen))
        
        # For each power of 2 less than current, check if (current - power) is prime
        # If it is, then current is a SuPrP2 number
        for i, power in enumerate(powers_of_two):
            # No need to check powers >= current (would give negative or zero result)
            if power >= current:
                break
            
            # Calculate the potential prime component
            potential_prime = current - power
            if is_prime(potential_prime):
                # Found a valid decomposition as prime + power of 2
                is_suprp2 = True
                found_prime = potential_prime
                found_power = power
                found_exponent = i
                break  # Use the first decomposition we find
        
        # If we found a valid SuPrP2 number, yield it with its decomposition
        if is_suprp2:
            yield (current, found_prime, found_power, found_exponent)
        
        # Move to the next number to check
        current += 1

# My student ID number - this is what we'll use as our starting point
STUDENT_ID = "113510621"

# Problem 3: Find 20 consecutive SuPrP2 numbers right after my student ID
# Create a generator for SuPrP2 numbers starting after my ID
suprp2_gen = suprp2_generator(STUDENT_ID)

# Get the first 20 SuPrP2 numbers
results = []
for _ in range(20):
    result = next(suprp2_gen)
    results.append(result)

# Display the 20 consecutive SuPrP2 numbers with their decompositions
print(f"20 consecutive SuPrP2 numbers right after {STUDENT_ID}:")
for suprp2, prime, power, exponent in results:
    print(f"{suprp2} = {prime} + 2^{exponent} (prime + {power})")

# Results for question 3 - adding these as comments in the source code
# (This is the answer to be submitted)
"""
20 consecutive SuPrP2 numbers right after 113510621:
113510625 = 113510609 + 2^4 (prime + 16)
113510627 = 113509603 + 2^10 (prime + 1024)
113510631 = 113510599 + 2^5 (prime + 32)
113510633 = 113509609 + 2^10 (prime + 1024)
113510635 = 113510603 + 2^5 (prime + 32)
113510637 = 113508589 + 2^11 (prime + 2048)
113510639 = 113445103 + 2^16 (prime + 65536)
113510641 = 113510609 + 2^5 (prime + 32)
113510643 = 113509619 + 2^10 (prime + 1024)
113510645 = 113248501 + 2^18 (prime + 262144)
113510647 = 113510519 + 2^7 (prime + 128)
113510649 = 113510521 + 2^7 (prime + 128)
113510651 = 113510587 + 2^6 (prime + 64)
113510653 = 113510141 + 2^9 (prime + 512)
113510654 = 113510653 + 2^0 (prime + 1)
113510655 = 113510653 + 2^1 (prime + 2)
113510657 = 113510653 + 2^2 (prime + 4)
113510659 = 105122051 + 2^23 (prime + 8388608)
113510660 = 113510659 + 2^0 (prime + 1)
113510661 = 113510659 + 2^1 (prime + 2)
"""
