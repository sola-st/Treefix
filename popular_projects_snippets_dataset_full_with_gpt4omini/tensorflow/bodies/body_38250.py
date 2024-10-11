# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
# num_rows * num_bins less than half of max shared memory.
num_rows = 128
num_cols = 27
size = 10
self._test_bincount_col_count(num_rows, num_cols, size, dtype)
