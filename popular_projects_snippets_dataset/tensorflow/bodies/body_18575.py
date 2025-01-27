# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
exit(control_flow_ops.while_loop(
    lambda j, x: j < 4,
    lambda j, x: (j + 1, x + i), [0, 0]))
