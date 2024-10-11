# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable(0, name="upto")
    self.assertAllEqual(v.count_up_to(1), 0)
    with self.assertRaises(errors.OutOfRangeError):
        v.count_up_to(1)
