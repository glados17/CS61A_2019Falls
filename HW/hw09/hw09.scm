
; Tail recursion

; (define (replicate-m x n m)
;   (if (= n 0) '()
;       (if (= n m) `()
;       (cons x (replicate-m x n (+ m 1)))))
;   )

; (define (replicate x n)
;     (replicate-m x n 0)
;    )
; learned form https://github.com/sgalal/cs61a/blob/master/Homework/hw06/hw06.scm
  (define (replicate x n)
  (define (helper n acc)
    (if (= n 0)
      acc
      (helper (- n 1) (cons x acc))))
  (helper n nil))


(define (accumulate-helper combiner n term)
  (if (= n 1) (term 1)
      (combiner (term n) (accumulate-helper combiner (- n 1) term))
))

(define (accumulate combiner start n term)
    (combiner start (accumulate-helper combiner n term))
  )

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


; learned form https://github.com/sgalal/cs61a/blob/master/Homework/hw06/hw06.scm 
(define (accumulate-tail combiner start n term)
  (define (helper x acc)
    (if (> x n)
      acc
      (helper (+ 1 x) (combiner acc (term x)))))
  (helper 1 start))

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ 3 x)) multiples-of-three))
)


(define (nondecreastream s)
    (if (>=(car-stream s) (car-stream (cdr-stream s)))
    ()
    () ))


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))