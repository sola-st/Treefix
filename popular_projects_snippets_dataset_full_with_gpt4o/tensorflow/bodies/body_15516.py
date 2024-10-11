# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Returns a shape that is broadcast-compatible with self & lengths.

    * If dimension[axis] is uniform and lengths is a scalar, the check
      that either lengths==1 or axis==1 or lengths==axis, and tile
      dimension[axis] with tf.where(lengths==axis, 1, axis) repeats.

    * If dimension[axis] is uniform and lengths is a vector, then check
      that dimension[axis]==1, and raggedly tile dimension[axis] with
      lengths repeats.  (we can skip tiling if we statically know that
      slice_lengths == 1??)

    * If dimension[axis] is ragged and lengths is a scalar, then check
      that lengths==1.

    * If dimension[axis] is ragged and lengths is a vector, then check
      that self.dimension_size(axis) == lengths.

    Args:
      axis: `int`.  The dimension to broadcast.
      lengths: 0-D or 1-D integer `Tensor`.

    Returns:
      A `RaggedTensorDynamicShape`.
    """
lengths = ragged_util.convert_to_int_tensor(
    lengths, name='lengths', dtype=self.dim_size_dtype)
# Check whether lengths is a scalar (for uniform dimensions) or
# vector (for ragged dimensions).
if lengths.shape.ndims is None:
    raise ValueError('lengths must have a known rank.')
elif lengths.shape.ndims > 1:
    raise ValueError('lengths must be a scalar or vector')
else:
    lengths_is_scalar = (lengths.shape.ndims == 0)

# Verify that the shapes are compatible.
if self.is_ragged(axis):
    if lengths_is_scalar:
        condition = math_ops.equal(lengths, 1)
    else:
        condition = math_ops.reduce_all(
            math_ops.equal(lengths, self.dimension_size(axis)))
else:
    axis_dim_size = self.dimension_size(axis)
    if lengths_is_scalar:
        condition = (
            math_ops.equal(lengths, 1) | math_ops.equal(axis_dim_size, 1)
            | math_ops.equal(axis_dim_size, lengths))
    else:
        condition = math_ops.equal(axis_dim_size, 1)
broadcast_err = [
    'Unable to broadcast: dimension size mismatch in dimension', axis,
    'lengths=', lengths, 'dim_size=',
    self.dimension_size(axis)
]
broadcast_check = control_flow_ops.Assert(
    condition, data=broadcast_err, summarize=10)

with ops.control_dependencies([broadcast_check]):
    # Partitioned dimensions:
    if axis < self.num_partitioned_dimensions:
        if self.is_ragged(axis):
            # Use an identity op to make sure the check actually gets run.
            exit(RaggedTensorDynamicShape(
                self._partitioned_dim_sizes,
                array_ops.identity(self.inner_dim_sizes), self.dim_size_dtype))
        else:
            exit(self._broadcast_uniform_partitioned_dimension(axis, lengths))

      # Inner dimensions:
    else:
        if lengths_is_scalar:
            exit(self._broadcast_inner_dimension_to_uniform(axis, lengths))
        else:
            if axis == 0:
                raise ValueError('Unable to broadcast: '
                                 'outermost dimension must be uniform.')
            exit(self._broadcast_inner_dimension_to_ragged(axis, lengths))
