# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
updated = ta.write(ta.size(), x)
# Here, capture empty_ta from outside the function.  However, it may be
# either a TF1-style TensorArray or an Eager-style TensorArray.
next_iter = control_flow_ops.cond(
    math_ops.equal(x % 3, 0), lambda: empty_ta, lambda: updated)
exit((next_iter, updated.stack()))
