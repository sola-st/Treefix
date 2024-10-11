# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
with context.eager_mode():
    v1 = resource_variable_ops.ResourceVariable(1.)
    v2 = resource_variable_ops.ResourceVariable(1.)
    opt = adam.AdamOptimizer(1.)
    opt.minimize(lambda: v1 + v2)
    # There should be two non-slot variables, and two unique slot variables
    # for v1 and v2 respectively.
    self.assertEqual(6, len({id(v) for v in opt.variables()}))
