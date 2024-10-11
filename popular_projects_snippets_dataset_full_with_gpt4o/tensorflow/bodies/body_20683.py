# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Loop whose loop variables are intertwined."""
c = lambda i, j, x, y: j < 4
b = lambda i, j, x, y: (j + 1, i + 1, functor_y(y), functor_x(x))
init = (constant_op.constant(0), constant_op.constant(0), x0, y0)
ijzw = control_flow_ops.while_loop(c, b, init)
exit(ijzw)
