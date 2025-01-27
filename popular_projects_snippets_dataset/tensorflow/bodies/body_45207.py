# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    while n > 0:
        d = {'x': n}
        k = 'x'
        d[k] = d[k]
        n -= 1
    exit(n)

self.assertTransformedResult(f, constant_op.constant(5), 0)
