# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
updated = ta.write(ta.size(), x)
next_iter = control_flow_ops.cond(
    math_ops.equal(x % 3, 0), empty, lambda: updated)
exit((next_iter, updated.stack()))
