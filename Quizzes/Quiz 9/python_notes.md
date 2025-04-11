# Python Programming Notes

## Scope Resolution (LEGB Rule)
Python follows the LEGB rule for variable lookup:
1. **L**ocal - Inside current function
2. **E**nclosing - Inside enclosing functions
3. **G**lobal - At module level
4. **B**uilt-in - Python's built-in names

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Uses local x
    
    inner()  # Prints: local
    print(x)  # Prints: enclosing

outer()
print(x)  # Prints: global
```

## Class Initialization (`__init__`)
- Special method called when creating new instances
- First parameter is always `self` (refers to the instance)
- Used to set up initial state of objects

```python
class Student:
    def __init__(self, name, id):
        self.name = name  # Instance variable
        self.id = id
        self.grades = []  # Default value

# Creating instance
student = Student("Alice", "12345")
```

## Variable Types
1. **Class Variables**
   - Shared among all instances
   - Defined at class level
   ```python
   class University:
       purpose = "Learning"  # Class variable
   ```

2. **Instance Variables**
   - Unique to each instance
   - Created in `__init__` using `self`
   ```python
   def __init__(self, name):
       self.name = name  # Instance variable
   ```

3. **Local Variables**
   - Only accessible within their scope
   - Created inside functions/methods

4. **Global Variables**
   - Accessible throughout module
   - Use `global` keyword to modify inside functions

## Best Practices
1. **Avoid Global Variables**
   ```python
   # Bad
   global_var = 0
   
   # Good
   class Counter:
       def __init__(self):
           self.count = 0
   ```

2. **Use `self` Consistently**
   - Always use `self` for instance variables
   - Makes code clearer and prevents scope issues

3. **Class Design**
   - Clear purpose for each class
   - Proper initialization in `__init__`
   - Use instance variables for unique data
   - Use class variables for shared data

## String and List Operations
1. **String Immutability**
   ```python
   s = "Hello"
   # s[0] = 'h'  # Error
   s = 'h' + s[1:]  # Create new string
   ```

2. **List Mutability**
   ```python
   my_list = [1, 2, 3]
   my_list[0] = 10  # Valid
   my_list.append(4)
   ```

## Regular Expressions
```python
import re

text = "Student ID: 112-00-0001"
pattern = r"Student ID: (\d{3}-\d{2}-\d{4})"
match = re.search(pattern, text)
if match:
    student_id = match.group(1)
```

## Key Takeaways
1. Understand scope hierarchy (LEGB)
2. Use `__init__` for proper object initialization
3. Distinguish between class and instance variables
4. Follow Python naming conventions
5. Document your code
6. Use appropriate data structures
7. Handle exceptions properly
8. Write clean, readable code 