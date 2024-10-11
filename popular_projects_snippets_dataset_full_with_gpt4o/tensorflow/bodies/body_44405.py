# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i, s
i = constant_op.constant(2)
raise ValueError('testing')
s = i ** 5  # pylint: disable=unreachable
