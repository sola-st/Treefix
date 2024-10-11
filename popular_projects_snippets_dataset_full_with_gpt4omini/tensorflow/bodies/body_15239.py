# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""The total size of a dimension (like nvals).

      This is a static version of DynamicRaggedShape._num_slices_in_dimension()

      Example:

      ```
      shape = DynamicRaggedShape.Spec(
        _row_partitions=[
          RowPartitionSpec(nrows=3, nvals=14, dtype=tf.int32)
          RowPartitionSpec(nrows=14, nvals=25, dtype=tf.int32)

        ],
        _static_inner_shape=tf.TensorShape([25, 3, 4]),
        _inner_shape=tf.TensorSpec(tf.TensorShape([3]), dtype=tf.int32))
      shape._num_slices_in_dimension(0) = 3
      shape._num_slices_in_dimension(1) = 14
      shape._num_slices_in_dimension(2) = 25
      shape._num_slices_in_dimension(3) = 3
      shape._num_slices_in_dimension(4) = 4
      shape._num_slices_in_dimension(-2) = 3
      ```

      Args:
        axis: the last dimension to include.

      Returns:
        the number of values in a dimension.
      """
if not isinstance(axis, int):
    raise TypeError("axis must be an integer")
axis = array_ops.get_positive_axis(axis, self.rank, ndims_name="rank")

if axis == 0:
    exit(self._dimension(0))
if axis <= self.num_row_partitions:
    # TODO(martinz): use nvals OR nrows, whichever is defined.
    exit(self._row_partitions[axis - 1].nvals)
remainder = axis - (self.num_row_partitions - 1)
head_inner_shape = self._static_inner_shape[:remainder]
exit(head_inner_shape.num_elements())
