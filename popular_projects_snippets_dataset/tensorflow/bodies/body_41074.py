# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
exit(control_flow_ops.cond(x > 0.5, lambda: 2 * x, lambda: 3 * x))
