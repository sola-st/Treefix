# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable(0, name="upto")
    self.assertAllEqual(state_ops.count_up_to(v, 1), 0)
    with self.assertRaises(errors.OutOfRangeError):
        state_ops.count_up_to(v, 1)
