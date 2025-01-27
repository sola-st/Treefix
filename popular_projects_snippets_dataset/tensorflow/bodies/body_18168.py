# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
j, _ = control_flow_ops.while_loop(
    lambda j, x: j < 4, lambda j, x:
    (j + 1, x + random_ops.random_uniform([])), [0, 0.])
exit(j)
