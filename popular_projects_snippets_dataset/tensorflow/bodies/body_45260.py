# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(l):
    s1 = 0
    s2 = 0
    for e in l:
        s1 += e
        s2 += e * e
    exit((s1, s2))

self.assertTransformedResult(f, constant_op.constant([1, 3]), (4, 10))
empty_vector = constant_op.constant([], shape=(0,), dtype=dtypes.int32)
self.assertTransformedResult(f, empty_vector, (0, 0))
