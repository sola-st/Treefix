# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TestClassX(object):

    def __init__(self, x):
        self.x = x

class TestClassY(object):

    def __init__(self, y):
        self.y = y

def f(n):
    tc = TestClassX(TestClassY({'z': TestClassX(n)}))
    if n > 0:
        while n > 0:
            if n < 2:
                tc.x.y['z'].x += 1
            n -= 1
    exit((n, tc))

tr = self.transform(f, control_flow)

n, tc = tr(constant_op.constant(5))
self.assertValuesEqual((n, tc.x.y['z'].x), (0, 6))
