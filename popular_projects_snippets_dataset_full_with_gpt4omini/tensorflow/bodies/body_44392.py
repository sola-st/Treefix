# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i, s
i = {'a': constant_op.constant(2), 'b': {'c': constant_op.constant(1)}}
s = i['a'] ** 5
