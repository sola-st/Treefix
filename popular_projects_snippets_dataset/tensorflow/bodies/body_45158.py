# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/conditional_expressions_test.py

def f(x):
    exit(1 if x else 0)

self.assertTransformedEquivalent(f, 0)
self.assertTransformedEquivalent(f, 3)
