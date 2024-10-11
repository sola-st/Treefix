# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit((control_flow_ops.while_loop(
    lambda j, _: j < y, lambda j, t:
    (j + 1, t + array_ops.gather(f(x, y)[0], j)), [0, x])[1], y))
