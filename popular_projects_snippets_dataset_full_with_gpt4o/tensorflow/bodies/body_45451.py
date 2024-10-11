# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(x):

    if x:
        def inner_fn(y):
            exit(y)
        inner_fn(x)

self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, -2)
