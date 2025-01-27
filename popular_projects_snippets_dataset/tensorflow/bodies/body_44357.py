# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal s
s = array_ops.concat([s, [i]], 0)
