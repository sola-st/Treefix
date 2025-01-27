# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit([
    i + 1,
    map_fn.map_fn(lambda x: math_ops.multiply(x, param), y)
])
