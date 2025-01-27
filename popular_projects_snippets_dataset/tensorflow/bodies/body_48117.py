# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Unpack validation data based input type.

  The validation data is not touched if its dataset or dataset iterator.
  For other type of input (Numpy or tensor), it will be unpacked into tuple of
  3 which is x, y and sample weights.

  Args:
    validation_data: dataset, dataset iterator, or numpy, tensor tuple.
    raise_if_ambiguous: boolean on whether to fail if validation_data cannot be
      parsed. Otherwise simply return validation_data, None, None and defer the
      decision to the caller.

  Returns:
    tuple of 3, (x, y, sample_weights) for numpy and tensor input.
  """
if (isinstance(validation_data, (iterator_ops.Iterator,
                                 iterator_ops.IteratorBase,
                                 dataset_ops.DatasetV2,
                                 data_utils.Sequence))
    or not hasattr(validation_data, '__len__')):
    val_x = validation_data
    val_y = None
    val_sample_weight = None
elif len(validation_data) == 2:
    try:
        val_x, val_y = validation_data  # pylint: disable=unpacking-non-sequence
        val_sample_weight = None
    except ValueError:
        val_x, val_y, val_sample_weight = validation_data, None, None
elif len(validation_data) == 3:
    try:
        val_x, val_y, val_sample_weight = validation_data  # pylint: disable=unpacking-non-sequence
    except ValueError:
        val_x, val_y, val_sample_weight = validation_data, None, None
else:
    if raise_if_ambiguous:
        raise ValueError(
            'When passing a `validation_data` argument, '
            'it must contain either 2 items (x_val, y_val), '
            'or 3 items (x_val, y_val, val_sample_weights), '
            'or alternatively it could be a dataset or a '
            'dataset or a dataset iterator. '
            'However we received `validation_data=%s`' % validation_data)
    val_x, val_y, val_sample_weight = validation_data, None, None
exit((val_x, val_y, val_sample_weight))
