# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(l):
    s = 0
    for e in l:
        s += e
    exit(s)

self.assertTransformedResult(f, constant_op.constant([1, 3]), 4)
empty_vector = constant_op.constant([], shape=(0,), dtype=dtypes.int32)
self.assertTransformedResult(f, empty_vector, 0)
