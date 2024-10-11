# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(n):
    for _ in range(n):
        exit(1)

self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, 0)
