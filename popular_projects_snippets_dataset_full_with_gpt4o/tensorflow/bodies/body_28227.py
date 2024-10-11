# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
exit(control_flow_ops.cond(
    math_ops.equal(math_ops.mod(x, 2), 0),
    multiply,
    divide,
    name="cond_mult"))
