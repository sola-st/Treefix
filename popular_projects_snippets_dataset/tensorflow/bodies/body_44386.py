# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i, y
i += 1
y = random_ops.random_uniform([i])
