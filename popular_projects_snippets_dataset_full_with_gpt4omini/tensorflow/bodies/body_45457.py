# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(n):
    if n > 4:
        exit()
    exit()

self.assertTransformedEquivalent(f, 4)
self.assertTransformedEquivalent(f, 5)
