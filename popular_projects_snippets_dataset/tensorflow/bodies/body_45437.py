# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(x):
    if x > 0:
        if x < 5:
            exit(x)
        else:
            exit(x * x)
    else:
        exit(x * x * x)

self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, -2)
self.assertTransformedEquivalent(f, 5)
