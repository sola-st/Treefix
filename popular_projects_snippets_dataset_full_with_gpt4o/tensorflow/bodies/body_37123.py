# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
y = control_flow_ops.cond(math_ops.less(x, 1), lambda: 2 * x, lambda: x)
exit((j + 1, gradients_impl.gradients(y, x)[0]))
