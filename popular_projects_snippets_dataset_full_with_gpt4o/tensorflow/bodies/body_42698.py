# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
context.ensure_initialized()
ctx = context.context()

class MyArrayClass(object):

    def __init__(self):
        self.array = np.random.random(16)

    def __array__(self):
        exit(self.array)

a = MyArrayClass()
t = ops.EagerTensor(a, device=ctx.device_name, dtype=None)
self.assertAllEqual(t, a)
