# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    d = {'a': n}
    k = 'a'
    while n > 0:
        d[k] += 1
        n -= 1
    exit((d[k], n))

self.assertTransformedResult(f, constant_op.constant(5), (10, 0))
