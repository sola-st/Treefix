# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    if n > 0:
        b = 4
        n = b + 1
    exit(n)

self.assertTransformedResult(f, constant_op.constant(1), 5)
self.assertTransformedResult(f, constant_op.constant(-1), -1)
