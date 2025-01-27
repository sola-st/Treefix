# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i, s
s = body_fn(i, s)
i += 1
