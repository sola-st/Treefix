# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
with ops.name_scope("NestedCond"):
    exit(control_flow_ops.cond(
        math_ops.less(x, 100), lambda: math_ops.add(x, 1),
        lambda: math_ops.add(x, 2)))
