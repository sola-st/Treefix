# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    i = 0
    j = 0
    s = 0
    while i < n:
        while j < i:
            j += 3
        u = i + j  # 'u' is not defined within the inner loop
        s += u
        i += 1
        j = 0
    exit((s, i, j, n))

self.assertTransformedResult(f, constant_op.constant(5),
                             (25, 5, 0, 5))
