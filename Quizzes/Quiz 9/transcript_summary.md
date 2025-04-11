# CS 3323 Python Programming Review

## 1. Python Programming Basics

### Text Processing and Regular Expressions
Python excels at text processing and manipulation. Here's an example of using regular expressions:

```python
import re

# Example of text processing with regular expressions
text = "Student ID: 112-00-0001, Name: Chris Carson"
pattern = r"Student ID: (\d{3}-\d{2}-\d{4})"
match = re.search(pattern, text)
if match:
    student_id = match.group(1)
    print(f"Found student ID: {student_id}")
```

### String Immutability
Strings in Python are immutable, meaning they cannot be changed after creation:

```python
# String immutability example
s = "Hello"
# s[0] = 'h'  # This would raise an error
s = 'h' + s[1:]  # Create a new string instead
print(s)  # Output: hello
```

### List Operations
Lists are mutable and support various operations:

```python
# List operations example
my_list = [1, 2, 3]
my_list[0] = 10  # Lists are mutable
my_list.append(4)  # Add element
my_list.extend([5, 6])  # Add multiple elements
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
```

## 2. Python Scope Rules

### Global vs Local Variables
Variables can exist in different scopes:

```python
# Global and local scope example
x = "global"  # Global variable

def my_function():
    x = "local"  # Local variable
    print(f"Inside function: {x}")

my_function()
print(f"Outside function: {x}")
# Output:
# Inside function: local
# Outside function: global
```

### Class Variables vs Instance Variables
Class variables are shared among all instances, while instance variables are unique to each object:

```python
class MyClass:
    class_var = "shared"  # Class variable
    
    def __init__(self):
        self.instance_var = "unique"  # Instance variable

obj1 = MyClass()
obj2 = MyClass()

print(f"Class variable (shared): {MyClass.class_var}")
print(f"Instance 1 variable: {obj1.instance_var}")
print(f"Instance 2 variable: {obj2.instance_var}")
```

### Scope Hierarchy
Python follows a specific order when looking up variables:

```python
x = "global"

class MyClass:
    x = "class"
    
    def __init__(self):
        self.x = "instance"
        
    def method(self):
        x = "local"
        print(f"Local x: {x}")
        print(f"Instance x: {self.x}")
        print(f"Class x: {MyClass.x}")
        print(f"Global x: {globals()['x']}")

obj = MyClass()
obj.method()
```

### Using `self` for Object Variables
The `self` keyword is crucial for accessing instance variables:

```python
class Person:
    def __init__(self, name):
        self.name = name  # Correct way to create instance variable
        
    def greet(self):
        print(f"Hello, my name is {self.name}")  # Access instance variable

person = Person("Alice")
person.greet()
```

## 3. Class Implementation

### Basic Class Structure
Here's a complete example of a class implementation:

```python
class University:
    # Class variable (shared among all instances)
    purpose = "Learning"
    
    def __init__(self, name, location, president):
        # Instance variables (unique to each instance)
        self.name = name
        self.location = location
        self.president = president
    
    def is_good(self):
        # Instance method
        return self.location == "Norman"
    
    @classmethod
    def get_purpose(cls):
        # Class method
        return cls.purpose

# Creating instances
ou = University("University of Oklahoma", "Norman", "Joseph Harroz")
osu = University("Oklahoma State University", "Stillwater", "Kayse Shrum")

# Accessing instance variables
print(ou.name)  # Output: University of Oklahoma
print(osu.location)  # Output: Stillwater

# Accessing class variable
print(University.purpose)  # Output: Learning

# Using instance method
print(ou.is_good())  # Output: True
print(osu.is_good())  # Output: False
```

### Variable Deletion and Scope Resolution
Demonstrating how variable deletion affects scope:

```python
class Example:
    x = "class variable"
    
    def __init__(self):
        self.x = "instance variable"

# Create instances
e1 = Example()
e2 = Example()

print(f"Before deletion:")
print(f"e1.x: {e1.x}")  # Output: instance variable
print(f"e2.x: {e2.x}")  # Output: instance variable

# Delete instance variable
del e1.x

print(f"\nAfter deletion:")
print(f"e1.x: {e1.x}")  # Output: class variable
print(f"e2.x: {e2.x}")  # Output: instance variable
```

## 4. Best Practices

### Avoiding Global Variables
Instead of using global variables, use class variables or pass values as parameters:

```python
# Bad practice
global_var = 0

def increment():
    global global_var
    global_var += 1

# Good practice
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

counter = Counter()
counter.increment()
```

### Proper Use of `self`
Always use `self` to access instance variables and methods:

```python
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display_info(self):
        # Correct way to access instance variables
        print(f"Name: {self.name}, ID: {self.id}")
    
    def update_name(self, new_name):
        # Correct way to modify instance variables
        self.name = new_name
```

### Scope Management
Understanding and managing scope is crucial:

```python
class ScopeExample:
    class_var = "class"
    
    def __init__(self):
        self.instance_var = "instance"
        local_var = "local"  # This is local to __init__
    
    def method(self):
        # Can access instance and class variables
        print(self.instance_var)
        print(self.__class__.class_var)
        
        # Can't access local_var from __init__
        # print(local_var)  # This would raise an error
```

## 5. Key Takeaways

1. **Scope Hierarchy**:
   - Local scope (inside functions/methods)
   - Instance scope (self)
   - Class scope
   - Global scope
   - Built-in scope

2. **Variable Types**:
   - Class variables: Shared among all instances
   - Instance variables: Unique to each object
   - Local variables: Only accessible within their scope
   - Global variables: Accessible throughout the module

3. **Best Practices**:
   - Use `self` consistently for instance variables
   - Avoid global variables when possible
   - Understand scope resolution order
   - Use class variables for shared data
   - Use instance variables for unique data

4. **Class Design**:
   - Define clear purpose for classes
   - Use proper initialization
   - Implement appropriate methods
   - Follow Python naming conventions
   - Document your code 