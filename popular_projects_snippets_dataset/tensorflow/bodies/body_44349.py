# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal i
with ops.control_dependencies((control_flow_ops.Assert(i < 3, (i,)),)):
    i = it
