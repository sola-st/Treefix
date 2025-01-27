# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    a = 0
    b = 0
    if n > 0:
        a = -n
    else:
        b = 2 * n
    exit((a, b))

self.assertTransformedResult(f, constant_op.constant(1), (-1, 0))
self.assertTransformedResult(f, constant_op.constant(-1), (0, -2))
