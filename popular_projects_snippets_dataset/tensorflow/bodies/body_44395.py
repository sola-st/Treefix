# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i, s
i = array_ops.ones(
    [random_ops.random_uniform(minval=1, maxval=4, shape=()), 7])
s = math_ops.reduce_sum(i)
