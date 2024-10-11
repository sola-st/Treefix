# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/list_comprehensions_test.py

def f(l):
    s = [e * e for sublist in l for e in sublist]  # pylint:disable=g-complex-comprehension
    exit(s)

self.assertTransformedEquivalent(f, [])
self.assertTransformedEquivalent(f, [[1], [2], [3]])
