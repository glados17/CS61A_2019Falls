; The solutions for this part are learned from others'.


(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (cond
    ((null? rests) nil)
    (else (cons
      (append (cons first nil) (car rests))
      (cons-all first (cdr rests))))))

(define (zip pairs)
  (list (map car pairs) (map cadr pairs)))

;; Problem 16
;; Returns a list of two-element lists
; (define (enumerate s)
;   ; BEGIN PROBLEM 16
;   (define (enumerate_helper k output s)
;     (if (null? s) output
;     (enumerate_helper (+ k 1) (append output (list(cons k (list(car s))))) (cdr s))
;     ))
;   (enumerate_helper 0 nil s)
;   )
  ; END PROBLEM 16

(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (enumerate_helper k s)
    (if (eq? s nil) nil
    (cons (list k (car s)) (enumerate_helper (+ k 1) (cdr s)))
    ))
  (enumerate_helper 0 s)
  )


;; Problem 17
;; List all ways to make change for TOTAL with DENOMS



(define (list-change total denoms)
;   BEGIN PROBLEM 17
;  (cond ((or (null? denoms) (< total 0)) nil)
;   ((= total 0) (list ()))
;   (else 
;     (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))))

(cond ((or (< total 0) (null? denoms)) nil)
      ((= total 0) (list ()))
    
    (else (append 
          (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) 
          (list-change total (cdr denoms))
          ))
)
)

    ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda


(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
        ;  'replace-this-line
        expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
        ;  'replace-this-line
        expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
          ;  'replace-this-line
           (cons form (cons params (map let-to-lambda body)))   

           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
          ;  'replace-this-line
          (cons (cons 'lambda (cons (car (zip values)) (map let-to-lambda body))) (map let-to-lambda (cadr (zip values))))

           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
        ;  'replace-this-line
        (cons (car expr) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 18
         )))
