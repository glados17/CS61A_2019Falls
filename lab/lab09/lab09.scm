;; Scheme ;;

(define (over-or-under x y)
  (cond ((> x y) 1)
        ((< x y) -1)
        (else 0)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0
(define (filter-lst f lst)
  ; in fact this works :)
  ; (filter f lst) 
  (if (null? lst) 
      nil
      (if (f (car lst))
        (cons (car lst) (filter-lst f (cdr lst)) ) 
        (filter-lst f (cdr lst))
      )
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder num)
  (lambda (x) (+ x num))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
  '((1) 2 (3 4) 5)
)

(define (composed f g)
    (lambda (x) (f (g x)))
)

(define (remove item lst)
  (filter-lst (lambda (x) (not (equal? x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (if (null? s)
      s
      (cons (car s) (remove (car s) (no-repeats (cdr s))) )
  )
)

(define (substitute s old new)
  (if (null? s)
      s
      (cons
        (if (list? (car s))
            (substitute (car s) old new)
            (if (equal? (car s) old)
                new
                (car s)
            )
        )
        (substitute (cdr s) old new)
      )
  )
)

(define (sub-all s olds news)
  (if (null? olds)
    s
    (substitute (sub-all s (cdr olds) (cdr news)) (car olds) (car news))
  )
  
)