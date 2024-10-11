# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    ref = resource_variable_ops.ResourceVariable(
        [False, True, False], trainable=False)
    indices = math_ops.range(3)
    updates = constant_op.constant([True, True, True])
    state_ops.scatter_update(ref, indices, updates)
    self.assertAllEqual(ref.read_value(), [True, True, True])
