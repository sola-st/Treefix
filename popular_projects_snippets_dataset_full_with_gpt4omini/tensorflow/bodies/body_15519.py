# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Broadcasts the inner dimension `axis` to match `lengths`."""
dim_size = self.dimension_size(axis)
axis_in_inner_dims = axis - self.num_partitioned_dimensions
partitioned_sizes = self._partitioned_dim_sizes
inner_sizes = array_ops.concat([
    self._inner_dim_sizes[:axis_in_inner_dims],
    [array_ops.where(math_ops.equal(dim_size, 1), length, dim_size)],
    self._inner_dim_sizes[axis_in_inner_dims + 1:]
],
                               axis=0)
exit(RaggedTensorDynamicShape(partitioned_sizes, inner_sizes,
                                self.dim_size_dtype))
