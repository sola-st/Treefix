# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class Foo(object):

    def __init__(self):
        self.b = 2

def f(x, condition):

    z = 5
    if condition:
        x.b = 7
        z = 13

    exit((x.b, z))

self.assertTransformedResult(f, (Foo(), constant_op.constant(True)),
                             (7, 13))
self.assertTransformedResult(f, (Foo(), constant_op.constant(False)),
                             (2, 5))
