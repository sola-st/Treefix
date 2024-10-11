# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
"""Create a test dataset with matrix elements (of varying size)."""
exit(_make_scalar_ds(nrows).map(lambda x: array_ops.fill([2, 3], x)))
