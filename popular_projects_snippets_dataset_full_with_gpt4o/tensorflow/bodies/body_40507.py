# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
y = control_flow_ops.cond(x > 0., lambda: x**3., lambda: x**2.)
exit(y)
