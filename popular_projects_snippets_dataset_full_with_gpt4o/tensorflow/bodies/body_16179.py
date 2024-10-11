# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` with a specified partitioning for `values`.

    This constructor is private -- please use one of the following ops to
    build `RaggedTensor`s:

      * `tf.RaggedTensor.from_row_lengths`
      * `tf.RaggedTensor.from_value_rowids`
      * `tf.RaggedTensor.from_row_splits`
      * `tf.RaggedTensor.from_row_starts`
      * `tf.RaggedTensor.from_row_limits`
      * `tf.RaggedTensor.from_nested_row_splits`
      * `tf.RaggedTensor.from_nested_row_lengths`
      * `tf.RaggedTensor.from_nested_value_rowids`

    Args:
      values: A potentially ragged tensor of any dtype and shape `[nvals, ...]`.
      row_partition: A `RowPartition` object, representing the arrangement of
        the lists at the top level.
      internal: True if the constructor is being called by one of the factory
        methods.  If false, an exception will be raised.

    Raises:
      ValueError: If internal = False. Note that this method is intended only
                 for internal use.
      TypeError: If values is not a `RaggedTensor` or `Tensor`, or
                 row_partition is not a `RowPartition`.
    """

if not internal:
    raise ValueError("RaggedTensor constructor is private; please use one "
                     "of the factory methods instead (e.g., "
                     "RaggedTensor.from_row_lengths())")
_assert_is_supported_ragged_values_type(values)
if not isinstance(row_partition, RowPartition):
    raise TypeError(f"Argument `row_partition` must be a RowPartition. "
                    f"Received {row_partition}.")

# Validate shapes.
values.shape.with_rank_at_least(1)
if isinstance(values, RaggedTensor):
    # pylint: disable=protected-access
    assert row_partition.dtype == values._row_partition.dtype

self._values = values
self._row_partition = row_partition
