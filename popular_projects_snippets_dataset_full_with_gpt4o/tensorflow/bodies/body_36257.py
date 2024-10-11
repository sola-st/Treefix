# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with ops.device("/cpu:0"):
    a = x + x
    b = y + y
    exit(a + b)
