# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py

def f(x):
    v = []
    while x > 0:
        x -= 1
        if x % 2 == 0:
            break
        v.append(x)
    exit(v)

self.assertTransformedEquivalent(f, 0)
self.assertTransformedEquivalent(f, 1)
self.assertTransformedEquivalent(f, 4)
