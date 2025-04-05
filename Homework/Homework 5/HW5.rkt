#lang racket

; Name: Colby Frison
; Date: 3/31/2025
; Assignment: Homework 5
; Class: CS 3323


; Helper function to add two lists of numbers (polynomials in x)
; Takes two lists representing polynomials in x and adds them term by term
; Example: (add-lists '(1 2) '(3 4)) -> '(4 6)
(define (add-lists l1 l2)
  (cond
    [(null? l1) l2]                    ; If first list is empty, return second list
    [(null? l2) l1]                    ; If second list is empty, return first list
    [else (cons (+ (car l1) (car l2))  ; Add corresponding terms
                (add-lists (cdr l1) (cdr l2)))])) 

; Helper function to subtract two lists of numbers
; Takes two lists representing polynomials in x and subtracts them term by term
; Example: (sub-lists '(1 2) '(3 4)) -> '(-2 -2)
(define (sub-lists l1 l2)
  (cond
    [(null? l1) (map - l2)]            ; If first list is empty, negate all terms of second list
    [(null? l2) l1]                    ; If second list is empty, return first list
    [else (cons (- (car l1) (car l2))  ; Subtract corresponding terms
                (sub-lists (cdr l1) (cdr l2)))]))

; Helper function to multiply two lists (polynomials in x)
; Implements polynomial multiplication by distributing terms
; Example: (mul-lists '(1 2) '(3 4)) -> '(3 10 8)
(define (mul-lists l1 l2)
  (cond
    [(or (null? l1) (null? l2)) '()]   ; If either list is empty, result is empty
    [else
     (add-lists
      (map (lambda (x) (* x (car l1))) l2)  ; Multiply first term of l1 with all terms of l2
      (cons 0 (mul-lists (cdr l1) l2))) ; Recursively multiply rest of l1 with l2, shifted one position
     ]))

; Helper function to take derivative of a list with respect to x
; Applies the power rule for derivatives
; Example: (derx-list '(1 2 3)) -> '(2 6) (derivative of 1 + 2x + 3x²)
(define (derx-list l)
  (if (null? l)
      '()
      (let ([coeffs (cdr l)])          ; Skip constant term
        (if (null? coeffs)
            '()
            (map * (range 1 (add1 (length coeffs))) coeffs))))) ; Multiply each term by its power

; Helper function to remove trailing zeros
; Cleans up polynomial representation by removing unnecessary zero coefficients
; Example: (remove-trailing-zeros '(1 2 0 0)) -> '(1 2)
(define (remove-trailing-zeros lst)
  (cond
    [(null? lst) '()]
    [(null? (cdr lst)) (if (zero? (car lst)) '() lst)]
    [else
     (let ([rest (remove-trailing-zeros (cdr lst))])
       (if (and (zero? (car lst)) (null? rest))
           '()
           (cons (car lst) rest)))]))

; Helper function to clean empty or zero polynomials
; Removes empty lists from the end of polynomial representation
; Example: (clean-poly '((1 2) () () ())) -> '((1 2))
(define (clean-poly poly)
  (let ([cleaned (dropf-right poly null?)])     ; Remove trailing empty lists
    (if (null? cleaned)
        '()
        cleaned)))

; Main function for polynomial addition
; Adds two bivariate polynomials term by term
; Example: (poly_add '((1) (2)) '((3) (4))) -> '((4) (6))
(define (poly_add p1 p2)
  (clean-poly
   (cond
     [(null? p1) p2]                    ; If first polynomial is empty, return second
     [(null? p2) p1]                    ; If second polynomial is empty, return first
     [else
      (cons (remove-trailing-zeros (add-lists (car p1) (car p2)))  ; Add corresponding y-terms
            (poly_add (cdr p1) (cdr p2)))])))

; Main function for polynomial subtraction
; Subtracts second polynomial from first
; Example: (poly_sub '((1) (2)) '((3) (4))) -> '((-2) (-2))
(define (poly_sub p1 p2)
  (clean-poly
   (cond
     [(null? p1) (map (lambda (x) (map - x)) p2)]   ; If first poly empty, negate second poly
     [(null? p2) p1]                           ; If second poly empty, return first
     [else
      (cons (remove-trailing-zeros (sub-lists (car p1) (car p2)))  ; Subtract corresponding y-terms
            (poly_sub (cdr p1) (cdr p2)))])))

; Main function for polynomial multiplication
; Multiplies two bivariate polynomials using the distributive property
; Example: (poly_mul '((1) (1)) '((1) (1))) -> '((1) (2) (1))  ; (1 + y)(1 + y) = 1 + 2y + y²
(define (poly_mul p1 p2)
  (define (shift-poly p n)
    (if (zero? n)
        p
        (cons '() (shift-poly p (- n 1)))))
  
  (define (multiply-terms t1 t2)
    (remove-trailing-zeros (mul-lists t1 t2)))
  
  (define (multiply-with-shift term1 p2 shift)
    (shift-poly (map (lambda (term2) (multiply-terms term1 term2)) p2) shift))
  
  (define (multiply-terms-rec p1 p2 shift)
    (if (null? p1)
        '()
        (clean-poly
         (poly_add
          (multiply-with-shift (car p1) p2 shift)
          (multiply-terms-rec (cdr p1) p2 (+ shift 1))))))
  
  (clean-poly (multiply-terms-rec p1 p2 0)))

; Main function for partial derivative with respect to x
; Takes derivative of each x-polynomial coefficient
; Example: (poly_derx '((1 1) (2 2))) -> '((1) (2))  ; d/dx(1 + x + (2 + 2x)y) = 1 + 2y
(define (poly_derx poly)
  (clean-poly
   (map (lambda (term) (remove-trailing-zeros (derx-list term))) poly)))

; Test cases for all functions with expected results and mathematical notation
(printf "Testing add-lists:\n")
(printf "Test 1: (add-lists '(1 2) '(3 4)) = ~a\n" (add-lists '(1 2) '(3 4)))
(printf "Expected: '(4 6)\n")
(printf "Mathematical: (1 + 2x) + (3 + 4x) = 4 + 6x\n\n")

(printf "Test 2: (add-lists '() '(1 2)) = ~a\n" (add-lists '() '(1 2)))
(printf "Expected: '(1 2)\n")
(printf "Mathematical: 0 + (1 + 2x) = 1 + 2x\n\n")

(printf "Test 3: (add-lists '(1 2) '()) = ~a\n" (add-lists '(1 2) '()))
(printf "Expected: '(1 2)\n")
(printf "Mathematical: (1 + 2x) + 0 = 1 + 2x\n\n")

(printf "Test 4: (add-lists '(1 2 3) '(4 5)) = ~a\n" (add-lists '(1 2 3) '(4 5)))
(printf "Expected: '(5 7 3)\n")
(printf "Mathematical: (1 + 2x + 3x²) + (4 + 5x) = 5 + 7x + 3x²\n\n")

(printf "Test 5: (add-lists '(1) '(2 3 4)) = ~a\n" (add-lists '(1) '(2 3 4)))
(printf "Expected: '(3 3 4)\n")
(printf "Mathematical: 1 + (2 + 3x + 4x²) = 3 + 3x + 4x²\n\n")

(printf "Testing sub-lists:\n")
(printf "Test 1: (sub-lists '(1 2) '(3 4)) = ~a\n" (sub-lists '(1 2) '(3 4)))
(printf "Expected: '(-2 -2)\n")
(printf "Mathematical: (1 + 2x) - (3 + 4x) = -2 - 2x\n\n")

(printf "Test 2: (sub-lists '() '(1 2)) = ~a\n" (sub-lists '() '(1 2)))
(printf "Expected: '(-1 -2)\n")
(printf "Mathematical: 0 - (1 + 2x) = -1 - 2x\n\n")

(printf "Test 3: (sub-lists '(1 2) '()) = ~a\n" (sub-lists '(1 2) '()))
(printf "Expected: '(1 2)\n")
(printf "Mathematical: (1 + 2x) - 0 = 1 + 2x\n\n")

(printf "Test 4: (sub-lists '(1 2 3) '(4 5)) = ~a\n" (sub-lists '(1 2 3) '(4 5)))
(printf "Expected: '(-3 -3 3)\n")
(printf "Mathematical: (1 + 2x + 3x²) - (4 + 5x) = -3 - 3x + 3x²\n\n")

(printf "Test 5: (sub-lists '(1) '(2 3 4)) = ~a\n" (sub-lists '(1) '(2 3 4)))
(printf "Expected: '(-1 -3 -4)\n")
(printf "Mathematical: 1 - (2 + 3x + 4x²) = -1 - 3x - 4x²\n\n")

(printf "Testing mul-lists:\n")
(printf "Test 1: (mul-lists '(1 2) '(3 4)) = ~a\n" (mul-lists '(1 2) '(3 4)))
(printf "Expected: '(3 10 8)\n")
(printf "Mathematical: (1 + 2x)(3 + 4x) = 3 + 10x + 8x²\n\n")

(printf "Test 2: (mul-lists '() '(1 2)) = ~a\n" (mul-lists '() '(1 2)))
(printf "Expected: '()\n")
(printf "Mathematical: 0 * (1 + 2x) = 0\n\n")

(printf "Test 3: (mul-lists '(1 2) '()) = ~a\n" (mul-lists '(1 2) '()))
(printf "Expected: '()\n")
(printf "Mathematical: (1 + 2x) * 0 = 0\n\n")

(printf "Test 4: (mul-lists '(1) '(2 3 4)) = ~a\n" (mul-lists '(1) '(2 3 4)))
(printf "Expected: '(2 3 4)\n")
(printf "Mathematical: 1 * (2 + 3x + 4x²) = 2 + 3x + 4x²\n\n")

(printf "Test 5: (mul-lists '(1 2 3) '(4 5)) = ~a\n" (mul-lists '(1 2 3) '(4 5)))
(printf "Expected: '(4 13 22 15)\n")
(printf "Mathematical: (1 + 2x + 3x²)(4 + 5x) = 4 + 13x + 22x² + 15x³\n\n")

(printf "Testing derx-list:\n")
(printf "Test 1: (derx-list '(1 2 3)) = ~a\n" (derx-list '(1 2 3)))
(printf "Expected: '(2 6)\n")
(printf "Mathematical: d/dx(1 + 2x + 3x²) = 2 + 6x\n\n")

(printf "Test 2: (derx-list '()) = ~a\n" (derx-list '()))
(printf "Expected: '()\n")
(printf "Mathematical: d/dx(0) = 0\n\n")

(printf "Test 3: (derx-list '(1)) = ~a\n" (derx-list '(1)))
(printf "Expected: '()\n")
(printf "Mathematical: d/dx(1) = 0\n\n")

(printf "Test 4: (derx-list '(0 1 2 3)) = ~a\n" (derx-list '(0 1 2 3)))
(printf "Expected: '(1 4 9)\n")
(printf "Mathematical: d/dx(x + 2x² + 3x³) = 1 + 4x + 9x²\n\n")

(printf "Testing remove-trailing-zeros:\n")
(printf "Test 1: (remove-trailing-zeros '(1 2 0 0)) = ~a\n" (remove-trailing-zeros '(1 2 0 0)))
(printf "Expected: '(1 2)\n")
(printf "Mathematical: 1 + 2x + 0x² + 0x³ = 1 + 2x\n\n")

(printf "Test 2: (remove-trailing-zeros '(1 2 3)) = ~a\n" (remove-trailing-zeros '(1 2 3)))
(printf "Expected: '(1 2 3)\n")
(printf "Mathematical: 1 + 2x + 3x² (no trailing zeros)\n\n")

(printf "Test 3: (remove-trailing-zeros '(0 0 0)) = ~a\n" (remove-trailing-zeros '(0 0 0)))
(printf "Expected: '()\n")
(printf "Mathematical: 0 + 0x + 0x² = 0\n\n")

(printf "Test 4: (remove-trailing-zeros '()) = ~a\n" (remove-trailing-zeros '()))
(printf "Expected: '()\n")
(printf "Mathematical: 0\n\n")

(printf "Testing clean-poly:\n")
(printf "Test 1: (clean-poly '((1 2) () () ())) = ~a\n" (clean-poly '((1 2) () () ())))
(printf "Expected: '((1 2))\n")
(printf "Mathematical: (1 + 2x) + 0y + 0y² + 0y³ = 1 + 2x\n\n")

(printf "Test 2: (clean-poly '()) = ~a\n" (clean-poly '()))
(printf "Expected: '()\n")
(printf "Mathematical: 0\n\n")

(printf "Test 3: (clean-poly '(() () ())) = ~a\n" (clean-poly '(() () ())))
(printf "Expected: '()\n")
(printf "Mathematical: 0 + 0y + 0y² = 0\n\n")

(printf "Test 4: (clean-poly '((1) (2) (3))) = ~a\n" (clean-poly '((1) (2) (3))))
(printf "Expected: '((1) (2) (3))\n")
(printf "Mathematical: 1 + 2y + 3y²\n\n")

(printf "Testing poly_add:\n")
(printf "Test 1: (poly_add '((1) (2)) '((3) (4))) = ~a\n" (poly_add '((1) (2)) '((3) (4))))
(printf "Expected: '((4) (6))\n")
(printf "Mathematical: (1 + 2y) + (3 + 4y) = 4 + 6y\n\n")

(printf "Test 2: (poly_add '() '((1) (2))) = ~a\n" (poly_add '() '((1) (2))))
(printf "Expected: '((1) (2))\n")
(printf "Mathematical: 0 + (1 + 2y) = 1 + 2y\n\n")

(printf "Test 3: (poly_add '((1) (2)) '()) = ~a\n" (poly_add '((1) (2)) '()))
(printf "Expected: '((1) (2))\n")
(printf "Mathematical: (1 + 2y) + 0 = 1 + 2y\n\n")

(printf "Test 4: (poly_add '((1 2) (3)) '((4) (5 6))) = ~a\n" (poly_add '((1 2) (3)) '((4) (5 6))))
(printf "Expected: '((5 2) (8 6))\n")
(printf "Mathematical: (1 + 2x + 3y) + (4 + (5 + 6x)y) = 5 + 2x + (8 + 6x)y\n\n")

(printf "Test 5: (poly_add '((1) (2 3)) '((4 5) (6))) = ~a\n" (poly_add '((1) (2 3)) '((4 5) (6))))
(printf "Expected: '((5 5) (8 3))\n")
(printf "Mathematical: (1 + (2 + 3x)y) + ((4 + 5x) + 6y) = (5 + 5x) + (8 + 3x)y\n\n")

(printf "Testing poly_sub:\n")
(printf "Test 1: (poly_sub '((1) (2)) '((3) (4))) = ~a\n" (poly_sub '((1) (2)) '((3) (4))))
(printf "Expected: '((-2) (-2))\n")
(printf "Mathematical: (1 + 2y) - (3 + 4y) = -2 - 2y\n\n")

(printf "Test 2: (poly_sub '() '((1) (2))) = ~a\n" (poly_sub '() '((1) (2))))
(printf "Expected: '((-1) (-2))\n")
(printf "Mathematical: 0 - (1 + 2y) = -1 - 2y\n\n")

(printf "Test 3: (poly_sub '((1) (2)) '()) = ~a\n" (poly_sub '((1) (2)) '()))
(printf "Expected: '((1) (2))\n")
(printf "Mathematical: (1 + 2y) - 0 = 1 + 2y\n\n")

(printf "Test 4: (poly_sub '((1 2) (3)) '((4) (5 6))) = ~a\n" (poly_sub '((1 2) (3)) '((4) (5 6))))
(printf "Expected: '((-3 2) (-2 -6))\n")
(printf "Mathematical: (1 + 2x + 3y) - (4 + (5 + 6x)y) = -3 + 2x + (-2 - 6x)y\n\n")

(printf "Test 5: (poly_sub '((1) (2 3)) '((4 5) (6))) = ~a\n" (poly_sub '((1) (2 3)) '((4 5) (6))))
(printf "Expected: '((-3 -5) (-4 3))\n")
(printf "Mathematical: (1 + (2 + 3x)y) - ((4 + 5x) + 6y) = (-3 - 5x) + (-4 + 3x)y\n\n")

(printf "Testing poly_mul:\n")
(printf "Test 1: (poly_mul '((1) (1)) '((1) (1))) = ~a\n" (poly_mul '((1) (1)) '((1) (1))))
(printf "Expected: '((1) (2) (1))\n")
(printf "Mathematical: (1 + y)(1 + y) = 1 + 2y + y²\n\n")

(printf "Test 2: (poly_mul '() '((1) (2))) = ~a\n" (poly_mul '() '((1) (2))))
(printf "Expected: '()\n")
(printf "Mathematical: 0 * (1 + 2y) = 0\n\n")

(printf "Test 3: (poly_mul '((1) (2)) '()) = ~a\n" (poly_mul '((1) (2)) '()))
(printf "Expected: '()\n")
(printf "Mathematical: (1 + 2y) * 0 = 0\n\n")

(printf "Test 4: (poly_mul '((1 2) (3)) '((4) (5 6))) = ~a\n" (poly_mul '((1 2) (3)) '((4) (5 6))))
(printf "Expected: '((4 8) (17 16 12) (15 18))\n")
(printf "Mathematical: (1 + 2x + 3y)(4 + (5 + 6x)y) = 4 + 8x + (17 + 16x + 12x²)y + (15 + 18x)y²\n\n")

(printf "Test 5: (poly_mul '((1 2) (3)) '((4 5) (6))) = ~a\n" (poly_mul '((1 2) (3)) '((4 5) (6))))
(printf "Expected: '((4 13 10) (18 27) (18))\n")
(printf "Mathematical: (1 + 2x + 3y)((4 + 5x) + 6y) = (4 + 13x + 10x2) + (18y + 27xy) + (18y2)\n\n")

(printf "Testing poly_derx:\n")
(printf "Test 1: (poly_derx '((1 1) (2 2))) = ~a\n" (poly_derx '((1 1) (2 2))))
(printf "Expected: '((1) (2))\n")
(printf "Mathematical: d/dx(1 + x + (2 + 2x)y) = 1 + 2y\n\n")

(printf "Test 2: (poly_derx '()) = ~a\n" (poly_derx '()))
(printf "Expected: '()\n")
(printf "Mathematical: d/dx(0) = 0\n\n")

(printf "Test 3: (poly_derx '((1))) = ~a\n" (poly_derx '((1))))
(printf "Expected: '()\n")
(printf "Mathematical: d/dx(1) = 0\n\n")

(printf "Test 4: (poly_derx '((0 1 2) (3 4))) = ~a\n" (poly_derx '((0 1 2) (3 4))))
(printf "Expected: '((1 4) (4))\n")
(printf "Mathematical: d/dx(x + 2x² + (3 + 4x)y) = 1 + 4x + 4y\n\n")

(printf "Test 5: (poly_derx '((1 2 3) (4 5 6))) = ~a\n" (poly_derx '((1 2 3) (4 5 6))))
(printf "Expected: '((2 6) (5 12))\n")
(printf "Mathematical: d/dx(1 + 2x + 3x² + (4 + 5x + 6x²)y) = 2 + 6x + (5 + 12x)y\n")

