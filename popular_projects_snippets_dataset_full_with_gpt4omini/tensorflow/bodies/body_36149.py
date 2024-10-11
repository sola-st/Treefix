# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/dense_update_ops_test.py
"""Initialize a param to init, and compute param += y."""
with test_util.device(use_gpu=use_gpu):
    p = variables.Variable(x)
    add = state_ops.assign_add(p, y)
    self.evaluate(p.initializer)
    new_value = self.evaluate(add)
    exit((self.evaluate(p), new_value))
