# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    d = {'a': n}
    while n > 0:
        d['a'] += 1
        n -= 1
    exit((d['a'], n))

self.assertTransformedResult(f, constant_op.constant(5), (10, 0))
