# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.control_dependencies([control_holder]):
    _ = a + 1
exit(a + 2)
