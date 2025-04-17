def demonstrate_list_comprehensions():
    # Basic list comprehension with numbers
    numbers = [2*x for x in range(1,50)]
    print("First two elements:", numbers[0:2])
    print("First three elements:", numbers[0:3])
    print("Last element:", numbers[-1])

def demonstrate_string_manipulation():
    # List comprehension with strings and filtering
    states = [4*x+"tx" for x in "oklahoma" if x != "h"]
    print("Modified states:", states)
    print("Last three elements:", states[-3:-1])
    
    # String multiplication examples
    print("String multiplication:", 2*"oklahoma" + 3 * "texas")
    print("Last character of 'oklahoma':", "oklahoma"[-1])

def demonstrate_lambda_basics():
    # Basic lambda function demonstration
    def f(x):
        return lambda y: 2*x + y
    
    result = f("colorado")("ID")
    print("Lambda function result with strings:", result)

    result = f(5)(5)
    print("Lambda function result with numbers:", result)

def demonstrate_variable_scope():
    # Demonstrating variable scope in Python
    x = 5
    y = 7
    if (y==7):
        x= "oklahoma"
    print("Value of x after conditional:", x)

    def f():
        x = "texas"
    f()
    print("Value of x after function call:", x)

    def f():
        #print("Value of x:", x) causes error because x is not defined in the local scope
        x = "kansas"
        print("Value of x in local scope:", x)
    
    print("Value of x before function call:", x)
    f()
    print("Value of x after function call:", x)

def demonstrate_currying():
    # Example 1: Using nested lambda functions
    curried_add = lambda x: lambda y: x + y
    add_five = curried_add(5)  # Returns a function that adds 5 to its argument
    result = add_five(3)       # 5 + 3 = 8
    print("Curried addition result:", result)

    # Example 2: Using regular function definitions
    def multiply(x):
        def inner(y):
            return x * y
        return inner
    
    multiply_by_three = multiply(3)
    result = multiply_by_three(4)  # 3 * 4 = 12
    print("Curried multiplication result:", result)

    # Example 3: Currying with multiple arguments
    def curry_three_args(x):
        def inner(y):
            def innermost(z):
                return x + y + z
            return innermost
        return inner
    
    add_three_numbers = curry_three_args(1)(2)(3)  # 1 + 2 + 3 = 6
    print("Curried three-argument addition result:", add_three_numbers)

def demonstrate_referential_transparency():
    # Example of referential transparency
    def add(a, b):
        return a + b
    
    result = add(5, 3)
    print("Result of add function:", result)

    # Explanation of referential transparency
    print("\nReferential Transparency Explanation:")
    print("1. Functions are first-class objects in Python")
    print("2. Functions can be passed as arguments, returned from functions, and stored in data structures")
    print("3. Function calls can be replaced with their results without changing program behavior")
    print("4. This allows for more flexible and reusable code")

def demonstrate_lambda():
    print("\n=== Lambda Basics ===")
    demonstrate_lambda_basics()
    
    print("\n=== Variable Scope ===")
    demonstrate_variable_scope()
    
    print("\n=== Currying ===")
    demonstrate_currying()
    
    print("\n=== Referential Transparency ===")
    demonstrate_referential_transparency()

def main():
    print("========= List Comprehension Examples =========")
    demonstrate_list_comprehensions()
    print("\n")
    
    print("========= String Manipulation Examples =========")
    demonstrate_string_manipulation()
    print("\n")
    
    print("========= Lambda Function Examples =========")
    demonstrate_lambda()
    print("\n")
    

if __name__ == "__main__":
    main()






