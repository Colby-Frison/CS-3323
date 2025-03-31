#lang racket

;Notes on Recursion and lazy evaluation


;Factorial
(define (fac n)
    (if (= n 0)
        1
        (* (fac (- n 1)) n)
    )
)

;Tail Recursion Factorial
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

;Add One
(define (addone l)
    (if (null? l)
        '()
        (cons (+ (car l) 1) (addone (cdr l)))
    )
)

;; trail recursion
(define (TR_addone l)
    (letrec
        ((helper (lambda (result l)
            (if (null? l)
                result
                (helper (append result (list (+ (car l) 1))) (cdr l))))))
        (helper '() l)
    )
)

;??
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

;Reverse
(define (rev l)
    (if (null? l)
        l
        (append (rev (cdr l))
            (list (car l))
        )
    )
)

;Remove Zero
(define (rmzero l)
    (if (null? l)
        l
        (if (= (car l) 0)
            (rmzero (cdr l))
            l
        )
    )
)

;??
(define (sml a l)
    (if (null? l)
        l
        (cons (* a (car l))
            (sml a (cdr l))
        )
    )
)

(define lazy_int
    (letrec
        ((next (lambda (n) (cons n (delay (next (+ n 1)))))))
        (next 1)
    )
)

(define lazy_square
    (letrec
        ((next (lambda (n) (cons (* n n) (delay (next (+ n 1)))))))
        (next 1)
    )
)

(TR_addone '(5 7 8))