# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n):
    if n > 0:
        n = n + 1
        raise ValueError()
    exit(n)

self.assertTransformedResult(f, -3, -3)

tr = self.transform(f, control_flow)

with self.assertRaises(ValueError):
    tr(1)
