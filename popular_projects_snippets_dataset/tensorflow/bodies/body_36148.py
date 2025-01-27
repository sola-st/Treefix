# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/dense_update_ops_test.py
"""Initialize a param to init and update it with y."""
super(AssignOpTest, self).setUp()
with test_util.device(use_gpu=use_gpu):
    p = variables.Variable(x)
    assign = state_ops.assign(p, y)
    self.evaluate(p.initializer)
    new_value = self.evaluate(assign)
    exit((self.evaluate(p), new_value))
