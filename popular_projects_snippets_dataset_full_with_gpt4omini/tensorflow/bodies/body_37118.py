# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
z = v * 2
exit((i + 1, gradients_impl.gradients(z, x)[0]))
