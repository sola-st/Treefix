# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
z = math_ops.add(x, y)
exit(math_ops.mul(x, z))
