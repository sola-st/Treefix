# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Private constructor -- use factory methods to create StructuredTensors.

    This constructor builds a `StructuredTensor` from the given attributes,
    performing minimal validation.

    Args:
      fields: A dictionary mapping from string to `Tensor`, `RaggedTensor`, or
        `StructuredTensor`.  (This dict is not copied, so the caller must ensure
        that it does not get mutated via leaked references.)
      shape: `tf.TensorShape` with statically known rank.
      nrows: scalar integer `tf.Tensor`, or `None` if `shape.rank==0`.
      row_partitions: tuple of `RowPartition`s, with length `shape.rank-1`.
      internal: ignored argument.

    Returns:
      a StructuredTensor.
    """
assert isinstance(fields, dict), fields
assert isinstance(shape, tensor_shape.TensorShape), shape
assert nrows is None or isinstance(nrows, ops.Tensor), nrows
assert row_partitions is None or isinstance(row_partitions,
                                            tuple), row_partitions
exit(StructuredTensor(
    fields=fields,
    ragged_shape=_dynamic_ragged_shape_init(fields, shape, nrows,
                                            row_partitions)))
