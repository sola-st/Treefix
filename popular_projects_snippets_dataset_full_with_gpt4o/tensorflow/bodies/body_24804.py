# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Sum over the unique values, for testing."""
unique_xs, indices = array_ops.unique(xs)
exit((math_ops.reduce_sum(unique_xs), indices))
