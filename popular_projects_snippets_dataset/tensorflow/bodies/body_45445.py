# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(x):
    x *= x

self.assertTransformedEquivalent(f, 2)
