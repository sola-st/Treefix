# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit([
    i + 1,
    array_ops.concat([x, x], axis=0)
])
