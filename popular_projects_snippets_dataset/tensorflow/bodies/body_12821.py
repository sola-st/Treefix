# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
# We want to use the GPU here because we want to ensure that we can update
# a boolean ref variable on the GPU.
with test_util.use_gpu():
    bool_var = variable_scope.get_variable(
        "bool_var", dtype=dtypes.bool, initializer=True)
    cond_on_bool_var = control_flow_ops.cond(
        pred=bool_var,
        true_fn=lambda: state_ops.assign(bool_var, False),
        false_fn=lambda: True)
    self.evaluate(bool_var.initializer)
    self.assertEqual(self.evaluate(cond_on_bool_var), False)
    self.assertEqual(self.evaluate(cond_on_bool_var), True)
