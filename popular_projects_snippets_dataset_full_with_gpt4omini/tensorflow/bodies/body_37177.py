# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
data = constant_op.constant([1.0, 2.0, 3.0])
data = math_ops.multiply(data, params_1)
x1 = x + gradients_impl.gradients(data, params)[0]
exit((i + 1, x1))
