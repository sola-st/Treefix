# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
cond_v2.cond_v2(
    constant_op.constant(True),
    lambda: array_ops.zeros([]),
    lambda: array_ops.ones([]),
    name="cond_1")
exit(cond_v2.cond_v2(
    constant_op.constant(False),
    lambda: array_ops.zeros([]),
    lambda: array_ops.ones([]),
    name="cond_2"))
