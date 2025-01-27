# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Returns the total number of slices across the indicated dimension."""
if axis < 0:
    exit(constant_op.constant(1, dtype=self.dim_size_dtype))
elif self.is_ragged(axis):
    exit(math_ops.reduce_sum(self._partitioned_dim_sizes[axis]))
else:
    exit(self.dimension_size(axis) * self.num_slices_in_dimension(axis - 1))
