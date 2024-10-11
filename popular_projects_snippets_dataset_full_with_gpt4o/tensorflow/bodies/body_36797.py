# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.device("/device:CPU:1"):
    c = math_ops.add(a, a, name="c")
exit(c)
