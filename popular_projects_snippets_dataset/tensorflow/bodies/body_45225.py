# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TestClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

def f(n, obj):
    obj.a = 0
    obj.b = 0
    if n > 0:
        obj.a = -n
    else:
        obj.b = 2 * n
    exit(obj)

tr = self.transform(f, control_flow)

res_obj = tr(constant_op.constant(1), TestClass(0, 0))
self.assertValuesEqual((res_obj.a, res_obj.b), (-1, 0))
res_obj = tr(constant_op.constant(-1), TestClass(0, 0))
self.assertValuesEqual((res_obj.a, res_obj.b), (0, -2))
