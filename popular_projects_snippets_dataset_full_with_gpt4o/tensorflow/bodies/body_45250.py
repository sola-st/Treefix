# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(i):
    def inner_fn():
        nonlocal n
        if i == 0:
            n = i - 1

    n = 3
    inner_fn()
    exit(n)

self.assertTransformedResult(f, 1, 3)
self.assertTransformedResult(f, 0, -1)
