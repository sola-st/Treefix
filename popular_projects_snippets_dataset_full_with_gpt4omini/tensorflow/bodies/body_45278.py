# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(l):
    res = 0
    for x in l:
        res += x
    else:
        res += 1
    exit(res)

self.assertTransformedEquivalent(f, [])
self.assertTransformedEquivalent(f, [1, 2])
