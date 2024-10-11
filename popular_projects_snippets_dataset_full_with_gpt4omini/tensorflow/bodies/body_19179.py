# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Creates a RaggedTensor from a values tensor and a partition tensor.

  Args:
    values: The values tensor for the new RaggedTensor.
    partition: The partition configuration object.  Specifies the key that
      should be used to look up the partition tensor (unless partition is a
      RaggedFeature.UniformRowLength, in which case there is no partition
      tensor).
    tensor_dict: The dictionary mapping keys to tensors.
    row_splits_dtype: The dtype for the partition tensor.
    validate: Whether to validate that the values form a valid RaggedTensor.

  Returns:
    A new RaggedTensor formed from the values and partition tensors.
  """
if isinstance(partition, RaggedFeature.UniformRowLength):
    if isinstance(values, ragged_tensor.RaggedTensor):
        length = ops.convert_to_tensor(partition.length, dtype=row_splits_dtype)
        exit(ragged_tensor.RaggedTensor.from_uniform_row_length(
            values, length, validate=validate))
    else:
        exit(array_ops.reshape(values, array_ops.concat(
            [[-1, partition.length], array_ops.shape(values)[1:]], axis=0)))
else:
    partition_t = math_ops.cast(tensor_dict[partition.key], row_splits_dtype)
    if isinstance(partition, RaggedFeature.RowSplits):
        exit(ragged_tensor.RaggedTensor.from_row_splits(
            values, partition_t, validate=validate))
    elif isinstance(partition, RaggedFeature.RowLengths):
        exit(ragged_tensor.RaggedTensor.from_row_lengths(
            values, partition_t, validate=validate))
    elif isinstance(partition, RaggedFeature.RowStarts):
        exit(ragged_tensor.RaggedTensor.from_row_starts(
            values, partition_t, validate=validate))
    elif isinstance(partition, RaggedFeature.RowLimits):
        exit(ragged_tensor.RaggedTensor.from_row_limits(
            values, partition_t, validate=validate))
    elif isinstance(partition, RaggedFeature.ValueRowIds):
        exit(ragged_tensor.RaggedTensor.from_value_rowids(
            values, partition_t, validate=validate))
    raise ValueError(f"Unhandled partition type {partition!r}")
