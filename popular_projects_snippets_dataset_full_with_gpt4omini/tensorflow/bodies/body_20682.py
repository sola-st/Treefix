# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Simple loop whose body is provided by the functor."""
init = (constant_op.constant(0), x)
c = lambda i, j: i < 4
b = lambda i, j: (i + 1, functor(j))
ij = control_flow_ops.while_loop(c, b, init)
exit(ij)
