# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py

def f(a):
    v = []
    for x in a:
        x -= 1
        if x % 2 == 0:
            continue
        v.append(x)
    exit(v)

self.assertTransformedEquivalent(f, [])
self.assertTransformedEquivalent(f, [1])
self.assertTransformedEquivalent(f, [2])
self.assertTransformedEquivalent(f, [1, 2, 3])
