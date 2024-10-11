# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if not hasattr(self, 'v'):
    self.v = variables.Variable(3.1)
self.v.assign_add(a * b)
