# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Validates that the first dim (batch size) of all tensors are equal or None.

  Args:
    tensors: list of tensors to check.
    columns: list of feature columns matching tensors. Will be used for error
      messaging.

  Raises:
    ValueError: if one of the tensors has a variant batch size
  """
# bath_size is a tf.compat.v1.Dimension object.
expected_batch_size = None
for i in range(0, len(tensors)):
    if tensors[i].shape.dims[0].value is not None:
        if expected_batch_size is None:
            bath_size_column_index = i
            expected_batch_size = tensors[i].shape.dims[0]
        elif not expected_batch_size.is_compatible_with(tensors[i].shape.dims[0]):
            raise ValueError(
                'Batch size (first dimension) of each feature must be same. '
                'Batch size of columns ({}, {}): ({}, {})'.format(
                    columns[bath_size_column_index].name, columns[i].name,
                    expected_batch_size, tensors[i].shape.dims[0]))
