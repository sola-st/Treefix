# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f(x):
    if x > 0:
        with ops.name_scope(''):
            exit(x * x)
    else:
        exit(x)

self.assertTransformedEquivalent(f, 2)
self.assertTransformedEquivalent(f, -2)
