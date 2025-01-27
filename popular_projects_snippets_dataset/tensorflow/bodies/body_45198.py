# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n, x):
    d = {}
    k = 'subkey'
    while n < 5:
        if n == 0:
            d[k] = x
        else:
            d[k] = d[k] + 1
        n += 1
    exit(d)

self.assertTransformedResult(f, (0, constant_op.constant(10)),
                             {'subkey': 14})
tr = self.transform(f, control_flow)
with self.assertRaisesRegex(
    ValueError, r"'d\[k\]' must be defined before the loop"):
    tr(constant_op.constant(0), 0)
