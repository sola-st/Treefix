# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Verify equality between static batch sizes.

  Args:
    tensors: iterable of input tensors.
    columns: Corresponding feature columns.

  Raises:
    ValueError: in case of mismatched batch sizes.
  """
# bath_size is a Dimension object.
expected_batch_size = None
for i in range(0, len(tensors)):
    batch_size = tensor_shape.Dimension(
        tensor_shape.dimension_value(tensors[i].shape[0]))
    if batch_size.value is not None:
        if expected_batch_size is None:
            bath_size_column_index = i
            expected_batch_size = batch_size
        elif not expected_batch_size.is_compatible_with(batch_size):
            raise ValueError(
                'Batch size (first dimension) of each feature must be same. '
                'Batch size of columns ({}, {}): ({}, {})'.format(
                    columns[bath_size_column_index].name, columns[i].name,
                    expected_batch_size, batch_size))
