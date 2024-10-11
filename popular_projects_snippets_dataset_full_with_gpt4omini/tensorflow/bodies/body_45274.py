# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(x):
    while x > 2:
        x /= 2
    else:
        x += 1
    exit(x)

self.assertTransformedEquivalent(f, 4)
self.assertTransformedEquivalent(f, 2)
