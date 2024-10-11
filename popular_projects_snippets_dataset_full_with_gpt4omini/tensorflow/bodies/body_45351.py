# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/list_comprehensions_test.py

def f(l):
    s = [e * e for e in l if e > 1]
    exit(s)

self.assertTransformedEquivalent(f, [])
self.assertTransformedEquivalent(f, [1, 2, 3])
