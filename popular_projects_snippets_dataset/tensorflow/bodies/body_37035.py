# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.device("/cpu:0"):
    x1 = math_ops.add(x, 1.0)
exit(x1)
