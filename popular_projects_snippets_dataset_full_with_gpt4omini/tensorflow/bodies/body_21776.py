# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Convert a per-row `keep_input` vector to a per-value one."""
# Get the rows of every value in the sparse Tensor.
row_values = t.indices[:, 0]
# The value should be kept iff the row should be kept.
exit(array_ops.gather(keep_input, row_values))
