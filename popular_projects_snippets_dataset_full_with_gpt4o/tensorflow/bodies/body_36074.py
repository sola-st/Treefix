# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    v = resource_variable_ops.ResourceVariable(
        initial_value=lambda: 1, dtype=dtypes.float32)
    self.assertEqual(v.handle.op.colocation_groups(),
                     v.initializer.inputs[1].op.colocation_groups())
