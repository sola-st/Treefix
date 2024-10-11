# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TestClass(object):
    pass

def f(n, x):
    tc = TestClass()
    while n < 5:
        if n == 0:
            tc.subattr = x
        else:
            tc.subattr = tc.subattr + 1
        n += 1
    exit(tc.subattr)

self.assertTransformedResult(f, (0, constant_op.constant(10)), 14)
tr = self.transform(f, control_flow)
with self.assertRaisesRegex(
    ValueError, "'tc.subattr' must be defined before the loop"):
    tr(constant_op.constant(0), 0)
