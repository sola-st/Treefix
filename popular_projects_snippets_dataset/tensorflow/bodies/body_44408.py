# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i
state.field = state.field * 10 + i
i += 1
