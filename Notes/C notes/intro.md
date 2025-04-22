# Notes on C/C++/Java

## C

> C is considered a **middle level language**

- This is because C sits between upper (python) and lower (assembly) level language
- C is the **only** middle level language
    - There is also *rust* and *go*, but they came long after c


- there are 3 main points when creating a language:
    - Expressive -> python
    - Efficient -> c
    - Correct    -> scheme/haskell

- As described above some languages play more to certain categories

### Efficiency
- it is important to keep these characteristics in mind when deciding what to make something in, as it is crucial to make sure efficiency is kept in mind.
    - For example C is used to write things like: OS kernels, Cores of apps, and compiler - this is because all of these things need to be efficient leading to the use of C

### Expressiveness
- different languages will also interpret the same expressions differently depending on how expressive they are...
    - For example in python expressions with numbers are evaluated like actual math equations, where as in C expressions are evaluated as is, leading to C commonly misinterpreting mathematical expressions

```
4 > 3 > 2

python = True
-> 4 is greater than 3 which is greater than 2

C = False
-> 4 is greater than 3 so its true => 1, 1 is not greater than 2 so false
-> 4 > 3 > 2 => 1 > 2 => False
```

### C behaviors
- in C variables are only given a very specific amount fo bitd
    - char: 8 bits (1 byte)
    - short: 16 bits (2 bytes)
    - **int: 32 bits (4 bytes)**
    - long: 32 or 64 bits (4 or 8 bytes)
    - long long: 64 bits (8 bytes)
    - float: 32 bits (4 bytes)
    - double: 64 bits (8 bytes)
    - long double: 80 or 128 bits (10 or 16 bytes)

#### Overflow
- If numbers are created and the number surpasses the amount fo bits designated it will create a negative number as there is **overflow**

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
This code demonstrates integer overflow behavior in C with char variables.
A char is 8 bits (1 byte) and can store values from -128 to 127.
When we assign 255 to char a, it overflows and becomes -1 because:
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

##### example with integer factorial


34! is 0 in c

#### Arrays
##### out of bound

```
# include <stdio.h>
void f(int i);

int main(){
    f(3);
}

void f(int i){
    int bb[3] = {1,2,3}

    int aa[-i];
    printf("%d\n", bb[2])
    printf("%d\n", bb[10])
    printf("%d\n", aa[10])
    printf("%d\n", aa[-10])
}

results:
3
32767
-4
9699328
```

explanation:
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


==use picture from phone for matrix stuff==

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

explanation:
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


