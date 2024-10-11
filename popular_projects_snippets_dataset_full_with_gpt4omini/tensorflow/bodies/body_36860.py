# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.device("CPU:0"):
    exit(arg + 1)
