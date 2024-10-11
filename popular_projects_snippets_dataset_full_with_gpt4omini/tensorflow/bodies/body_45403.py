# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py

def f(x):
    v = []
    u = []
    w = []
    while x > 0:
        x -= 1
        if x % 2 == 0:
            if x % 3 != 0:
                u.append(x)
            else:
                w.append(x)
                continue
        v.append(x)
    exit((v, u, w))

self.assertTransformedEquivalent(f, 0)
self.assertTransformedEquivalent(f, 1)
self.assertTransformedEquivalent(f, 3)
self.assertTransformedEquivalent(f, 4)
