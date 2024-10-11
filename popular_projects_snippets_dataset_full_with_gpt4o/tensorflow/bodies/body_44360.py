# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
nonlocal s
nonlocal t
s = array_ops.concat([s, [i]], 0)
t = Test(var=t.var + 1)
