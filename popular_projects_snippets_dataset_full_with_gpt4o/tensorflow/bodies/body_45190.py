# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TestClass(object):

    def __init__(self):
        self.x = constant_op.constant(3)

def f(n):
    tc = TestClass()
    while n > 0:
        tc.x += 1
        n -= 1
    exit(n)

self.assertTransformedResult(f, constant_op.constant(5), 0)
