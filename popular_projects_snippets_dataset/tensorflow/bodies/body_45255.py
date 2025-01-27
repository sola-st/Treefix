# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class Foo(object):

    def __init__(self):
        self.b = 2
        self.c = 3

def f(x, condition):

    z = 5
    if condition:
        x.b = 7
        x.c = 11
        z = 13

    exit((x.b, x.c, z))

self.assertTransformedResult(f, (Foo(), constant_op.constant(True)),
                             (7, 11, 13))
self.assertTransformedResult(f, (Foo(), constant_op.constant(False)),
                             (2, 3, 5))
