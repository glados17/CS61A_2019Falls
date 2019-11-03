; Sierpinski's Triangle (aka Sierpinski's Gasket).
(speed 0)
(rt 90)

; scm> (fd 100)
; scm> (rt 90)
; scm> (bk 100)

(define (line) (fd 100))

; scm> (line)
; scm> (line)
; scm> (line)

(define (twice fn) (fn) (fn))

; scm> (rt 90)
; scm> (twice line)

(define (repeat k fn)
  ; Repeat fn k times.
  (fn)
  (if (> k 1) (repeat (- k 1) fn)))

; Star: (repeat 5 (lambda () (begin (fd 100) (rt 144))))

(define (tri fn)
  ; Repeat fn 3 times, each followed by a 120 degree turn.
  (repeat 3 (lambda () (fn) (lt 120))))

; (tri line)

(define (sier d k)
  ; Draw three legs of Sierpinski's triangle to depth d.
  (tri (lambda ()
         (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
  ; Draw one leg of Sierpinski's triangle to depth d.
  (sier (/ d 2) (- k 1))
  (penup) (fd d) (pendown))

(sier 200 5)

