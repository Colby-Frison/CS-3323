#lang racket

(define cubic-numbers
  (letrec
    ((helper (lambda (n)
               (cons (* n n n) (delay (helper (+ n 1)))))))
    (helper 1)))

; Test the stream
(car cubic-numbers)                    ; Should return 1
(car (force (cdr cubic-numbers)))      ; Should return 8
(car (force (cdr (force (cdr cubic-numbers)))))  ; Should return 27

; Tail recursive function to square all elements in a list
(define (TR_sqr_list lst)
  (letrec
    ((helper (lambda (result l)
               (if (null? l)
                   result
                   (helper (append result (list (* (car l) (car l)))) (cdr l))))))
    (helper '() lst)))

; Test cases
(TR_sqr_list '(3 0 6))      ; Should return '(9 0 36)
(TR_sqr_list '(2 1 3 1))    ; Should return '(4 1 9 1)


