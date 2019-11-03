; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst) 
      (filter (lambda (a) (if (> a x) #t #f)) lst)
)

(define (longest-increasing-subsequence lst)
  ; the following skeleton is optional, remove if you like
  (if (null? lst)
      nil
      (begin (define first (car lst))
             (define rest (cdr lst))
             (define large-values-rest
                     (larger-values first rest))
             (define with-first (cons first (longest-increasing-subsequence large-values-rest)))
             (define without-first (longest-increasing-subsequence rest))
             (if (> (length with-first) (length without-first) )
                 with-first
                 without-first))))

; Derivative
(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond 
    ((number? expr)
     0)
    ((variable? expr)
     (if (same-variable? expr var)
         1
         0))
    ((sum? expr)
     (derive-sum expr var))
    ((product? expr)
     (derive-product expr var))
    ((exp? expr)
     (derive-exp expr var))
    (else
     'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))

(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond 
    ((=number? a1 0)                 a2)
    ((=number? a2 0)                 a1)
    ((and (number? a1) (number? a2)) (+ a1 a2))
    (else                            (list '+ a1 a2))))

(define (sum? x) (and (list? x) (eq? (car x) '+)))

(define (addend s) (cadr s))

(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond 
    ((or (=number? m1 0) (=number? m2 0))
     0)
    ((=number? m1 1)
     m2)
    ((=number? m2 1)
     m1)
    ((and (number? m1) (number? m2))
     (* m1 m2))
    (else
     (list '* m1 m2))))

(define (product? x)
  (and (list? x) (eq? (car x) '*)))

(define (multiplier p) (cadr p))

(define (multiplicand p) (caddr p))

(define (derive-sum expr var) (make-sum (derive (cadr expr) var) (derive (caddr expr) var)))

(define (derive-product expr var) (make-sum (make-product (derive (cadr expr) var) (caddr expr)) (make-product (derive (caddr expr) var) (cadr expr))))

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent) 
(cond 
    ((=number? base 0) 0)
    ((=number? exponent 0) 1)
    ((=number? exponent 1) base)
    ((and (number? base) (number? exponent)) (expt base exponent))
    (else 
      (list '^ base exponent))))

(define (base exp) (cadr exp))

; (define (base exp) (if (exp? exp) (cadr exp) 'Error))

(define (exponent exp) (caddr exp))

(define (exp? exp) (and (list? exp) (eq? (car exp) '^)))


(define x^2 (make-exp 'x 2))

(define x^3 (make-exp 'x 3))

(define (derive-exp exp var) (make-product (exponent exp) (make-exp (base exp) (make-sum (exponent exp) -1)) ))
