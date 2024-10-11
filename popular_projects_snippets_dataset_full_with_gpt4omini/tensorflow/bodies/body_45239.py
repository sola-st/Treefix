# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    if n > 0:
        b = 4  # pylint:disable=unused-variable
    exit(n)

self.assertTransformedResult(f, constant_op.constant(1), 1)
self.assertTransformedResult(f, constant_op.constant(-1), -1)
