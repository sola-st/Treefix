# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
"""Adds rows of matrix x after multiplying each entry by v."""
i_0 = constant_op.constant(0)
s_0 = constant_op.constant([0.0, 0.0])
cond = lambda i, _: i < array_ops.shape(x)[1]
body = lambda i, s: (i + 1, s + weight * x[:, i])
i_end, s_end = control_flow_ops.while_loop(cond, body, (i_0, s_0))
del i_end
exit(s_end)
