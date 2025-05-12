# Notes on C/C++/Java

## C

> C is considered a **middle level language**

- C is often referred to as a middle-level language because it bridges the gap between high-level languages like Python and low-level languages like Assembly. This means it provides a balance between the abstraction of high-level languages and the control over hardware that low-level languages offer. C allows programmers to write efficient code that can directly interact with hardware, making it ideal for system programming, such as operating system kernels and embedded systems.

- While C is a prominent middle-level language, other languages like Rust and Go have emerged, offering similar capabilities but with modern features and safety mechanisms. However, C remains a foundational language in computer science education and industry due to its simplicity and efficiency.

- When designing a programming language, three main aspects are often considered:
  - **Expressive**: Languages like Python are designed to be expressive, allowing developers to write code that is easy to read and understand.
  - **Efficient**: C is known for its efficiency, making it suitable for performance-critical applications.
  - **Correct**: Languages like Scheme and Haskell emphasize correctness, often through strong typing and functional programming paradigms.

- Different languages prioritize these aspects differently, and C's focus on efficiency makes it a popular choice for applications where performance is crucial.

### Efficiency
- Efficiency is a key consideration when choosing a programming language for a project. C is often used for tasks that require high performance, such as writing operating system kernels, core components of applications, and compilers. These tasks demand efficient use of resources, which C provides through its low-level capabilities and minimal runtime overhead.

### Expressiveness
- The expressiveness of a language affects how easily developers can translate their ideas into code. In Python, expressions involving numbers are evaluated in a way that closely resembles mathematical notation. In contrast, C evaluates expressions based on operator precedence and associativity, which can lead to unexpected results if not carefully considered.

```
4 > 3 > 2

python = True
-> 4 is greater than 3 which is greater than 2

C = False
-> 4 is greater than 3 so it's true => 1, 1 is not greater than 2 so false
-> 4 > 3 > 2 => 1 > 2 => False
```

### C behaviors
- In C, variables are allocated a specific number of bits, which determines the range of values they can store. Understanding these limits is crucial for writing correct and efficient C programs.
  - **char**: 8 bits (1 byte)
  - **short**: 16 bits (2 bytes)
  - **int**: 32 bits (4 bytes)
  - **long**: 32 or 64 bits (4 or 8 bytes)
  - **long long**: 64 bits (8 bytes)
  - **float**: 32 bits (4 bytes)
  - **double**: 64 bits (8 bytes)
  - **long double**: 80 or 128 bits (10 or 16 bytes)

#### Overflow
- Overflow occurs when a calculation exceeds the storage capacity of the data type. In C, this can lead to unexpected results, such as negative numbers appearing when positive values are expected.

##### Example with char bit limit
```
# include <stdio.h>

int main(){
    char a=255;
    char b =x;

    if (a==b)
        printf("%d\n", 3323);
    else
        printf("%d\n", 101);
}
```
Explanation:
This code demonstrates integer overflow behavior in C with char variables. A char is 8 bits (1 byte) and can store values from -128 to 127. When we assign 255 to char a, it overflows and becomes -1 because:
- 255 in binary is 11111111
- In two's complement (used for signed integers), 11111111 represents -1

When b is -5:
- a is -1 (from overflow)
- b is -5
- -1 != -5, so the else branch executes, printing 101

If b were -1:
- a would be -1 (from overflow)
- b would be -1
- -1 == -1, so the if branch executes, printing 3323

##### Example with integer factorial

34! is 0 in C due to overflow, as the result exceeds the maximum value an integer can store.

#### Arrays
##### Out of Bound

```
# include <stdio.h>
void f(int i);

int main(){
    f(3);
}

void f(int i){
    int bb[3] = {1,2,3};

    int aa[-i];
    printf("%d\n", bb[2]);
    printf("%d\n", bb[10]);
    printf("%d\n", aa[10]);
    printf("%d\n", aa[-10]);
}

results:
3
32767
-4
9699328
```

Explanation:
This example demonstrates C's behavior with array access and out-of-bounds memory access:

1. `bb[2]` - Normal access to the last element of array bb, which contains 3.

2. `bb[10]` - Out-of-bounds access. The array only has 3 elements (indices 0-2), but we're accessing index 10. C doesn't perform bounds checking, so instead of an error, it reads whatever value happens to be in memory at that location (in this case, 32767).

3. `aa[-i]` - This declaration is invalid in standard C. It attempts to create an array with a negative size (-3), which is undefined behavior. The compiler might accept it, but the behavior is unpredictable.

4. `aa[10]` and `aa[-10]` - Both are accessing memory relative to an improperly defined array, resulting in arbitrary values from memory locations that have nothing to do with our program's intended variables.

This example highlights why array bounds checking is important and is built into many higher-level languages. In C, accessing elements outside an array's bounds can:
- Return random values from memory
- Overwrite important data if you assign to those locations
- Cause program crashes
- Create security vulnerabilities like buffer overflows

It's the programmer's responsibility to ensure array indices stay within bounds in C.

#### Strings

```c
#include <stdio.h>

char *p2 = "Michigan";
char c;
printf("%d\n", *(p2+8));
while (c = *p2++)
    printf("%c", c+1);

char p1[] = "oklahoma";
char q1[] = "michigan";
char *p, *q;
p = p1;
q = q1;
while (*q++ = *p++);
printf("\n%s", q1);
```

Explanation:
This code demonstrates several important concepts in C string handling:

First part:
1. `char *p2 = "Michigan"` - Creates a string literal "Michigan" and assigns its address to pointer p2.
2. `printf("%d\n", *(p2+8))` - Accesses the character at index 8 of the string, which is the null terminator '\0' (ASCII value 0).
3. `while (c = *p2++)` - A loop that:
   - Assigns the current character that p2 points to into c
   - Increments p2 to point to the next character
   - Continues until c becomes '\0' (which evaluates to false)
4. `printf("%c", c+1)` - Prints each character after adding 1 to its ASCII value, effectively shifting each letter one position in the alphabet. "Michigan" becomes "Njdijhbo".

Second part:
1. `char p1[] = "oklahoma"` and `char q1[] = "michigan"` - Create character arrays initialized with strings.
2. `p = p1; q = q1;` - Assign the addresses of these arrays to pointers p and q.
3. `while (*q++ = *p++);` - This is the classic C string copy operation:
   - Copies a character from where p points to where q points
   - Increments both pointers
   - Continues until the null terminator is copied (which evaluates to false)
4. `printf("\n%s", q1)` - Prints the resulting string in q1, which is now "oklahoma" because the contents of p1 were copied into q1.

This example shows how C strings are manipulated through pointers and how the null terminator serves as both a string ending marker and a condition to terminate loops.

### Memory Management and Dangling References in C

> A **dangling reference** happens when a pointer points to memory that is no longer valid

- This is one of the most common bugs in C programming
- Unlike Python or Java, C requires manual memory management
- There is no automatic garbage collection in C

#### Three Main Ways to Create Dangling References:

1. **Returning Local Variables** (Stack Memory):
```c
int* bad_function() {
    int x = 10;
    return &x;    // BAD: x disappears after function ends
}
```

2. **Using Freed Memory** (Heap Memory):
```c
int* ptr = malloc(sizeof(int));
free(ptr);         // Memory is gone
*ptr = 10;        // BAD: ptr points to freed memory
```

3. **Multiple Pointers to Same Memory**:
```c
int* p1 = malloc(sizeof(int));
int* p2 = p1;     // Both point to same place
free(p1);         // Memory is gone
*p2 = 20;         // BAD: p2 points to freed memory
```

#### How C Memory Works
- C has two types of memory:
    - **Stack Memory**: For local variables (automatic cleanup)
    - **Heap Memory**: For dynamic memory (manual cleanup)

##### Stack Memory Example:
```c
void function() {
    int x = 10;   // Lives on stack
}                 // x is automatically cleaned up
```

##### Heap Memory Example:
```c
int* ptr = malloc(sizeof(int));   // Lives on heap
*ptr = 10;
// ... use the memory ...
free(ptr);                        // Must clean up manually
```

#### How to Avoid Dangling References
- Always set pointers to NULL after freeing:
    ```c
    free(ptr);
    ptr = NULL;    // Now we can check if ptr is NULL
    ```

- Check if pointer is NULL before using:
    ```c
    if (ptr != NULL) {
        *ptr = 42;    // Safe to use
    }
    ```

#### Memory Leaks
- A memory leak happens when we lose the pointer to allocated memory
- This means we can't free the memory anymore
- Example of creating a memory leak:
```c
void leak_example() {
    int* ptr = malloc(sizeof(int));
    ptr = malloc(sizeof(int));    // First malloc is lost forever
}
```

#### Why This Matters
- C gives you direct control over memory
- This makes C very efficient but also dangerous
- You must manage memory yourself:
    - Allocate when needed (malloc)
    - Free when done (free)
    - Avoid dangling references
    - Avoid memory leaks

#### Comparison with Python
- Python handles all of this automatically
- It uses garbage collection to:
    - Find unused memory
    - Free it automatically
    - Prevent dangling references
    - Clean up memory leaks
- This makes Python safer but slower than C

### Automatic Garbage Collection

> **Reference Counting** is one of the main ways programming languages handle memory automatically

- Reference counting works by keeping track of how many things point to a piece of memory
    - When something points to memory, the count goes up
    - When something stops pointing to memory, the count goes down
    - When count hits 0, memory can be deleted safely

- This is why Python is easier to use than C:
    - C: You must free memory yourself
    - Python: Memory is freed automatically when you stop using it
    - This prevents most memory leaks and dangling references

- However, reference counting has some important problems:
    - **Circular References**: If two objects point to each other, they'll never be freed
    - **Performance Cost**: Keeping track of references takes time and memory
    - **Unpredictable Timing**: Memory might be freed at unexpected moments

- Languages handle these problems differently:
    - Python uses reference counting + cycle detection
    - Java uses a different method called "mark and sweep"
    - C++ smart pointers use reference counting optionally
    - C has no automatic memory management at all

- When to use reference counting:
    - Good for: Simple memory patterns, real-time systems
    - Bad for: Complex object relationships, high-performance needs
    - That's why C avoids it: Too much overhead for system programming

### Variable Scope and Pointer Behavior

> In C, variables have different **scopes** (lifetimes) depending on where they are declared

#### Example of Scope and Pointer Issues
```c
int i = 3;
int *p = &i;
int *q;

void foo() { int n = 5; p = &n; }
void bar() { int m = 7; }

int main() {
    cout << *p << endl;    // prints 3
    foo();
    bar();
    cout << *p << endl;    // prints 7 (undefined behavior)
}
```

#### Why This Happens:
1. **Initial Setup**:
   - `i` is a global variable with value 3
   - `p` points to `i`
   - `q` is an uninitialized pointer

2. **First Print**:
   - `*p` prints 3 because p points to i

3. **After foo()**:
   - `n` is created with value 5
   - `p` is changed to point to `n`
   - When foo() ends, `n` is destroyed
   - `p` now points to invalid memory (dangling pointer)
   - The memory location where `n` was stored is now free

4. **After bar()**:
   - `m` is created with value 7
   - By coincidence, the compiler reuses the same memory location where `n` was
   - This is pure chance - the compiler happened to place `m` in the same spot
   - `p` is still pointing to this location (though it shouldn't be)
   - This is why we see 7, but it's completely accidental
   - We could just as easily see any other value, crash, or have any undefined behavior

#### Key Points:
- Local variables (like `n` and `m`) only exist while their function is running
- When a function ends, its local variables' memory is marked as "free to use"
- The compiler can reuse this freed memory for new variables
- Getting 7 is pure coincidence because:
    1. The memory where `n` was got reused for `m`
    2. `p` was still pointing to that location
    3. We got lucky that the memory wasn't used for something else
- This is undefined behavior - never rely on it!

#### Best Practice:
- Never return or store pointers to local variables
- Always initialize pointers
- Be careful about variable scope
- Check if pointers are valid before using them
- Remember: getting 7 in this example is luck, not guaranteed behavior
    - so in a practical  assessment the result would be undefined not a tangible answer


3 functional 2 python 2 C

