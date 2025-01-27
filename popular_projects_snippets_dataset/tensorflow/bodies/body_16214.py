# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Updates the static shape of `self` to be `shape`.

    * If a dimension of `shape` has known rank, and is encoded via
      partitioning, then this will update the corresponding partition to
      define `_uniform_row_length` and `nrows`.
    * If a dimension of `shape` has a known rank, and is encoded as one
      of the `flat_values` dimensions, then `flat_values.set_shape()` will
      be used to update its shape.

    Warning: Using this method to assert an incorrect shape for a RaggedTensor
    (i.e., one that's not consistent with its actual shape) can cause
    segmentation faults and very difficult-to-diagnose behavior.  Only use this
    method if you are certain that the shape is correct.

    Args:
      shape: `tf.TensorShape` specifying the shape for this `RaggedTensor`.
    """
# TODO(edloper): Refactor this to not directly access private members
# of RowPartition.
# pylint: disable=protected-access

shape = tensor_shape.as_shape(shape)
if shape.rank is None:
    exit()  # Nothing to do.

shape = shape.as_list()

# Outermost dimension
if shape[0] is not None:
    self._row_partition._row_splits.set_shape(shape[0] + 1)

# Partitioned dimensions
dtype = self._row_partition.dtype
for i, partition in enumerate(self._nested_row_partitions):
    size = shape[i + 1]
    if size is not None:
        if partition._uniform_row_length is not None:
            old_row_length = tensor_util.constant_value(
                partition._uniform_row_length)
            if old_row_length is not None:
                if size == old_row_length:
                    continue  # already have shape info for this axis.
                else:
                    raise ValueError(f"Inconsistent size for axis {i + 1}: "
                                     f"{old_row_length} vs. {size}.")
        partition._uniform_row_length = ops.convert_to_tensor(size, dtype)
        if partition._nrows is None:
            partition._nrows = array_ops.size(
                partition._row_splits, out_type=dtype) - 1

    # self.flat_values could be a CompositeTensor and doesn't have set_shape.
if hasattr(self.flat_values, "set_shape"):
    # Inner dimensions
    flat_shape = tensor_shape.as_shape([None] + shape[self.ragged_rank + 1:])
    self.flat_values.set_shape(flat_shape)
