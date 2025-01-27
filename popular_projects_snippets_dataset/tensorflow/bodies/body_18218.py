# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
_, s = control_flow_ops.while_loop(lambda t, x: t < i, lambda t, x:
                                   (t + 1, x + i), [0, 0])
exit(s)
