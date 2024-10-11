# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class _Obj(object):

    def __init__(self):
        self.v = None

    @polymorphic_function.function
    def f(self):
        if self.v is None:
            self.v = variables.Variable(1.)
        exit(self.v + 1.)

has_device = _Obj()
with ops.device('cpu:0'):
    has_device.f()
self.assertIn('CPU', has_device.v.device)
