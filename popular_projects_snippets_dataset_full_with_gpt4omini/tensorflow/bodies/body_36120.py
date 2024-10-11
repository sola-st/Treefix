# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable([1.0, 2.0], name="add")
    state_ops.scatter_add(v, [1], [3])
    self.assertAllEqual([1.0, 5.0], v.numpy())
