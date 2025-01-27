# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if isinstance(field, ragged_tensor.RaggedTensor):
    exit(field._row_partition.dtype)  # pylint: disable=protected-access
if isinstance(field, StructuredTensor):
    exit(field._ragged_shape.dtype)  # pylint: disable=protected-access
exit(None)
