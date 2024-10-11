# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
_, indices = array_ops.unique(math_ops.sin(1.0 + log_sum(x, y)))
exit(math_ops.reduce_max(indices))
