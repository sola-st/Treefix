# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(x):

    def inner_fn(y):
        if y > 0:
            exit(y * y)
        else:
            exit(y)

    exit(inner_fn(x))

self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, -2)
