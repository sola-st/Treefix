# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():
    tensor = constant_op.constant([1, 2, 3, 4, 5])
    self.assertAllEqual(isum(tensor).numpy(), [46, 47, 48, 49, 50])
