# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
exit(math_ops.reduce_sum(x[:, None] * mat * x[None, :]))
