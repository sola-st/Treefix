# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TestClass(object):
    pass

def f(n, x):
    tc = TestClass()
    for i in n:
        if i == 0:
            tc.x = x
        else:
            tc.x = tc.x + i
    exit(tc.x)

self.assertTransformedResult(f, (range(5), constant_op.constant(10)), 20)
tr = self.transform(f, control_flow)

with self.assertRaisesRegex(
    ValueError, "'tc.x' must be defined before the loop"):
    tr(constant_op.constant(list(range(5))), 0)
