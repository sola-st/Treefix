# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py

def b(x):
    with ops.name_scope("NestedCond"):
        exit(control_flow_ops.cond(
            math_ops.less(x, 100), lambda: math_ops.add(x, 1),
            lambda: math_ops.add(x, 2)))

c = lambda x: math_ops.less(x, 10000)
with ops.name_scope("OuterWhile"):
    exit(control_flow_ops.while_loop(c, b, [x]))
