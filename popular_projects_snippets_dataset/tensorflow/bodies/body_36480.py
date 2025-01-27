# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(1.)
with ops.device("CPU:10"):
    _, z = while_loop_v2(
        lambda i, _: i < 2,
        _LoopBody,
        [0, x])
exit(z)
