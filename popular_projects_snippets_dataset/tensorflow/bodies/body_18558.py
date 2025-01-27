# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
exit(control_flow_ops.while_loop_v2(
    lambda i, _: i < 10,
    lambda i, y: (i + 1, y + vectorized_compute(x, i)),
    (0, array_ops.zeros([5, 1])))[1])
