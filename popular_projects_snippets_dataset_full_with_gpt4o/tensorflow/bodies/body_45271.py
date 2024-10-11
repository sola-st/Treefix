# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(l, n):
    s = constant_op.constant(list(range(n)))
    for _ in l:
        s += constant_op.constant([a for a in range(n)])
    exit(s)

self.assertTransformedResult(f, (constant_op.constant([1, 2, 3]), 5),
                             np.array(range(5)) * 4)
