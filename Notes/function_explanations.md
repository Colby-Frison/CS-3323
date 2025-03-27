# Racket Function Explanations

## Basic Functions

### `fac` - Factorial
```racket
(define (fac n)
    (if (= n 0)
        1
        (* (fac (- n 1)) n)
    )
)
```
This function calculates the factorial of a number n recursively. For example:
- `(fac 5)` = 5 * 4 * 3 * 2 * 1 = 120
- `(fac 0)` = 1 (base case)
- `(fac 3)` = 3 * 2 * 1 = 6

### `trfac` - Tail Recursive Factorial
```racket
(define (trfac n) 
    (letrec
        ((helper (lambda (result m)
            (if (= m n) result
                (helper (* result (+ m 1)) (+ m 1))
            ))
        ))
        (helper 1 0)
    )
)
```
This is a more efficient version of factorial using tail recursion. It maintains an accumulator (`result`) to avoid building up the call stack. For example:
- `(trfac 5)` = 120
- `(trfac 3)` = 6

## List Operations

### `addone` - Add One to Each Element
```racket
(define (addone l)
    (if (null? l)
        '()
        (cons (+ (car l) 1) (addone (cdr l)))
    )
)
```
This function takes a list of numbers and adds 1 to each element. For example:
- `(addone '(1 2 3))` = '(2 3 4)
- `(addone '())` = '()

### `svadd` - Scalar Vector Addition
```racket
(define (svadd l1 l2)
    (if (null? l1)
        l2
        (if (null? l2)
            l1
            (cons
                (+ (car l1) (car l2))
                (svadd (cdr l1) (cdr l2))
            )
        )
    )
)
```
This function adds two lists element by element. For example:
- `(svadd '(1 2 3) '(4 5 6))` = '(5 7 9)
- `(svadd '(1 2) '(3))` = '(4 5)
- `(svadd '() '(1 2))` = '(1 2)

### `rev` - Reverse List
```racket
(define (rev l)
    (if (null? l)
        l
        (append (rev (cdr l))
            (list (car l))
        )
    )
)
```
This function reverses a list. For example:
- `(rev '(1 2 3))` = '(3 2 1)
- `(rev '())` = '()

### `rmzero` - Remove Zeros
```racket
(define (rmzero l)
    (if (null? l)
        l
        (if (= (car l) 0)
            (rmzero (cdr l))
            l
        )
    )
)
```
This function removes all zeros from the beginning of a list. For example:
- `(rmzero '(0 0 1 2 3))` = '(1 2 3)
- `(rmzero '(1 2 3))` = '(1 2 3)
- `(rmzero '(0 0 0))` = '()

### `sml` - Scalar Multiplication
```racket
(define (sml a l)
    (if (null? l)
        l
        (cons (* a (car l))
            (sml a (cdr l))
        )
    )
)
```
This function multiplies each element in a list by a scalar value. For example:
- `(sml 2 '(1 2 3))` = '(2 4 6)
- `(sml 3 '())` = '()

## Lazy Evaluation

### `lazy_int` - Lazy Integer Stream
```racket
(define lazy_int
    (letrec
        ((next (lambda (n) (cons n (delay (next (+ n 1)))))))
        (next 1)
    )
)
```
This creates an infinite stream of integers starting from 1. It uses `delay` to create a lazy evaluation, meaning values are only computed when needed. For example:
- `(car lazy_int)` = 1
- `(car (cdr (force (cdr lazy_int))))` = 3

### `lazy_square` - Lazy Square Stream
```racket
(define lazy_square
    (letrec
        ((next (lambda (n) (cons (* n n) (delay (next (+ n 1)))))))
        (next 1)
    )
)
```
This creates an infinite stream of perfect squares starting from 1. For example:
- `(car lazy_square)` = 1
- `(car (cdr (force (cdr lazy_square))))` = 9 