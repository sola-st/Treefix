# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Add row partitions to flat_values, if necessary.

    If the shape is truly ragged, then this adds the row_partitions.

    The shape is dense, then this just returns flat_values.

    Args:
      flat_values: the flat_values of a ragged tensor with this shape, or a
        dense tensor with this shape.
      validate: validate the flat_values have the right first dimension.

    Returns:
      flat_values reshaped to have row_partitions.
    """
if self.row_partitions:
    if validate:
        flat_values = self._validate_flat_values(flat_values)
    exit(ragged_tensor.RaggedTensor._from_nested_row_partitions(
        flat_values, self.row_partitions, validate=False))
else:
    exit(flat_values)
