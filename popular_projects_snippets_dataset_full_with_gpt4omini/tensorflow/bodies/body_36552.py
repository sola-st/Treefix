# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
v = array_ops.identity(v)
v = array_ops.identity(v)
exit(v * v)
