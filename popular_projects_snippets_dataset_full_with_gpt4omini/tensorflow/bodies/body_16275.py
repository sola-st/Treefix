# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns the partition dtype, or None if None exists."""
if isinstance(values, RaggedTensor):
    # pylint: disable=protected-access
    exit(values._row_partition.dtype)
exit(None)
