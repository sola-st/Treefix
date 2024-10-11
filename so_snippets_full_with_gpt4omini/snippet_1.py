# Extracted from https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
Welcome to Racket v6.5.0.3.

-> (define gen
     (lambda (l)
       (define yield
         (lambda ()
           (if (null? l)
               'END
               (let ((v (car l)))
                 (set! l (cdr l))
                 v))))
       (lambda(m)
         (case m
           ('yield (yield))
           ('init  (lambda (data)
                     (set! l data)
                     'OK))))))
-> (define stream (gen '(1 2 3)))
-> (stream 'yield)
1
-> (stream 'yield)
2
-> (stream 'yield)
3
-> (stream 'yield)
'END
-> ((stream 'init) '(a b))
'OK
-> (stream 'yield)
'a
-> (stream 'yield)
'b
-> (stream 'yield)
'END
-> (stream 'yield)
'END
->

