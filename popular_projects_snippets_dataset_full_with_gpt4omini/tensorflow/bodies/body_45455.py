# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(n):
    i = 0
    s = 0
    while i < n:
        i += 1
        s += i
        if s > 4:
            exit(s)
    exit(-1)

self.assertTransformedEquivalent(f, 0)
self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, 4)
