# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(x):
    if x > 0:
        exit(x)
    exit(x * x)

self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, -2)
