(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            ((y (expt x (expt 3 (- n 1)))))
            (* y y y))
            ))


(define-macro (def func bindings body)
    ; `(define ,(func bindings) ,body))
    `(define ,func (lambda ,bindings ,body)))
