# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(control_flow_ops.while_loop(
    lambda j, *_: j < i, lambda j, x, y, z, w:
    (j + 1, x + i, y + x, z, w), [
        0,
        constant_op.constant(0),
        constant_op.constant(1), i,
        constant_op.constant(2)
    ]))
