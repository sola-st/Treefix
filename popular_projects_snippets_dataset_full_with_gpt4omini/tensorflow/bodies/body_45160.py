# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/conditional_expressions_test.py

def f(x):
    y = x * x if x > 0 else x if x else 1
    exit(y)

self.assertTransformedEquivalent(f, -2)
self.assertTransformedEquivalent(f, 0)
self.assertTransformedEquivalent(f, 2)
