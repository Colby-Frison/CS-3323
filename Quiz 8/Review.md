# Scheme (Racket) Review

## Common Syntax

### Basic Operations
```scheme
; Comments start with semicolon
#lang racket  ; Language declaration

; Basic arithmetic
(+ 1 2)      ; Addition: 3
(- 5 2)      ; Subtraction: 3
(* 4 3)      ; Multiplication: 12
(/ 10 2)     ; Division: 5
(modulo 7 3) ; Modulo: 1

; Boolean operations
(and #t #f)  ; False
(or #t #f)   ; True
(not #t)     ; False

; Comparison
(= 1 1)      ; Equal: #t
(< 1 2)      ; Less than: #t
(> 3 2)      ; Greater than: #t
(<= 2 2)     ; Less than or equal: #t
(>= 3 2)     ; Greater than or equal: #t
```

### Function Definition
```scheme
; Basic function definition
(define (function-name param1 param2)
  body)

; Lambda expression (anonymous function)
(lambda (x) (* x x))

; Function with local variables
(define (func x)
  (let ([y 10])
    (* x y)))
```

### List Operations
```scheme
; List creation
(list 1 2 3)        ; Creates (1 2 3)
'(1 2 3)            ; Quote notation
(cons 1 '(2 3))     ; Adds element to front: (1 2 3)

; List access
(car '(1 2 3))      ; First element: 1
(cdr '(1 2 3))      ; Rest of list: (2 3)
(cadr '(1 2 3))     ; Second element: 2
(length '(1 2 3))   ; Length: 3

; List manipulation
(append '(1 2) '(3 4))  ; Combines lists: (1 2 3 4)
(reverse '(1 2 3))      ; Reverses list: (3 2 1)
(map add1 '(1 2 3))     ; Applies function: (2 3 4)
```

## Lazy Evaluation

Lazy evaluation is a strategy where expressions are evaluated only when their values are needed. In Scheme/Racket, this is primarily implemented using `delay` and `force`.

### Basic Lazy Evaluation
```scheme
; Creating a delayed computation
(define lazy-val (delay (begin
                         (display "Computing...")
                         (* 10 20))))

; Nothing is computed yet
; Only computed when forced:
(force lazy-val)  ; Displays "Computing..." and returns 200
(force lazy-val)  ; Just returns 200 (cached)
```

### Streams (Infinite Lists)
```scheme
; Define an infinite stream of numbers
(define (integers-from n)
  (cons n (delay (integers-from (+ n 1)))))

; Helper to force the next element
(define (stream-first s) (car s))
(define (stream-rest s) (force (cdr s)))

; Example usage
(define nums (integers-from 1))
(stream-first nums)          ; 1
(stream-first (stream-rest nums))  ; 2
```

## Tail Recursion

Tail recursion is a special case of recursion where the recursive call is the last operation in the function. Scheme optimizes tail-recursive functions to use constant stack space.

### Non-Tail Recursive vs Tail Recursive

```scheme
; Non-tail recursive factorial
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))  ; Must wait for recursive call

; Tail recursive factorial
(define (factorial-tail n)
  (define (fact-iter n acc)
    (if (= n 0)
        acc
        (fact-iter (- n 1) (* acc n))))  ; Recursive call is last operation
  (fact-iter n 1))

; Non-tail recursive sum
(define (sum lst)
  (if (null? lst)
      0
      (+ (car lst) (sum (cdr lst)))))  ; Must wait for recursive call

; Tail recursive sum
(define (sum-tail lst)
  (define (sum-iter lst acc)
    (if (null? lst)
        acc
        (sum-iter (cdr lst) (+ acc (car lst)))))  ; Recursive call is last operation
  (sum-iter lst 0))
```

### Identifying Tail Recursion
A function is tail recursive if:
1. The recursive call is the last operation to be performed
2. No computation depends on the result of the recursive call
3. The result of the recursive call is immediately returned

### Common Tail Recursive Patterns
```scheme
; Accumulator pattern
(define (length-tail lst)
  (define (length-iter lst acc)
    (if (null? lst)
        acc
        (length-iter (cdr lst) (+ acc 1))))
  (length-iter lst 0))

; Multiple accumulator pattern
(define (fib-tail n)
  (define (fib-iter n a b)
    (if (= n 0)
        a
        (fib-iter (- n 1) b (+ a b))))
  (fib-iter n 0 1))
```

## Common Higher-Order Functions

```scheme
; map: Apply function to each element
(map (lambda (x) (* x 2)) '(1 2 3))  ; (2 4 6)

; filter: Keep elements that satisfy predicate
(filter even? '(1 2 3 4))  ; (2 4)

; foldl: Accumulate from left to right
(foldl + 0 '(1 2 3))  ; 6

; foldr: Accumulate from right to left
(foldr cons '() '(1 2 3))  ; (1 2 3)
```
