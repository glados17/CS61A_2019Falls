; ;;;;;;;;;;;;;;
; ; Questions ;;
; ;;;;;;;;;;;;;;
; Scheme
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (sign x) 
    (cond ((> x 0) 1) ((= x 0) 0) ((< x 0) -1)
    )
)

(define (square x) (* x x))

(define (pow b n) 
    (if (= n 1) b
    (if (even? n) 
        (square (pow b (/ n 2))) 
        (* b (square (pow b (/ (- n 1) 2))))
        )
    )
    )
(define (unique s)
    (define (remove item lst)
        (filter (lambda (x) (not (equal? x item))) lst)
    )
    (if (null? s)
        s
        (cons (car s) (remove (car s) (unique (cdr s))) )
    )
) 
    
; (define (isnotin x s)
;     (if (< (length s) 1) #f (if (< (length s) 2) (not (= x (car s))) (or (isnotin x (cdr s) (not (= x (cars)))))))
;     )

; (define (unique s) 
;     (if (> (length s) 0)
;     (if (isnotin (car s),(cdr s)) (append (list(car s)) (unique (cdr s))))
;      ()
;     )
; )
