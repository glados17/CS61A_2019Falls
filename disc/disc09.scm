; takes two lists and concatenates them
; scm> (my-append '(1 2 3) '(2 3 4))
; (1 2 3 2 3 4)

(define (my-append a b) 
    (if (eq? (cdr a) nil) 
        (cons (car a) b) 
        (cons (car a) (my-append (cdr a) b)) ))

; t takes an element x and a non-negative integer n, and returns
; a list with x repeated n times.
; scm> (replicate 5 3)
; (5 5 5)

(define (replicate x n) 
    (if (eq? n 0) nil (cons x (replicate x (- n 1))) )
)

; A run-length encoding is a method of compressing a sequence of letters. The list
; (a a a b a a a a) can be compressed to ((a 3) (b 1) (a 4)), where the compressed
; version of the sequence keeps track of how many letters appear consecutively.
; Write a function that takes a compressed sequence and expands it into the original
; sequence. Hint: You may want to use my-append and replicate.
; scm> (uncompress '((a 1) (b 2) (c 3)))
; (a b b c c c)

(define (uncompress s) 
    (if (eq? (cdr s) nil) 
        (replicate (car (car s)) (car (cdr (car s)))) 
        (my-append (replicate (car (car s)) (car (cdr (car s))))  (uncompress (cdr s)))
        )
    
)

; Write a function that takes a procedure and applies it to every element in a given
; list.
; scm> (map (lambda (x) (* x x)) '(1 2 3))
; (1 4 9)

(define (map fn s)
    (if (eq? s nil)
    nil
    (cons (fn (car s)) (map fn (cdr s)))
    )
)

; Fill in the following to complete an abstract tree data type:
(define (make-tree label branches) (cons label branches))

(define (label tree) (car tree))

(define (branches tree) (cdr tree))

; 3 Using the abstract data type above, write a function that sums up the entries of a
; tree, assuming that the entries are all numbers.
; Hint: you may want to use the map function you defined above, and also write a
; helper function for summing up the entries of a list.

(define (sum-list s) 
    (if (eq? s nil)
    0
    (+ (car s) (sum-list (cdr s)))
    )
)






