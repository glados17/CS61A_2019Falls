; failed to work it out
; offical solution:

(define (partial-sums stream)
  (define (helper sum-so-far stream-remaining)
    (if (null? stream-remaining)
        nil
        (begin (define new-sum (+ sum-so-far (car stream-remaining)))
  	     (cons-stream new-sum (helper new-sum (cdr-stream stream-remaining))))))
  (helper 0 stream)
)