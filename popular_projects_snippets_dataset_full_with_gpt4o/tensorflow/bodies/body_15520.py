# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
axis_in_inner_dims = axis - self.num_partitioned_dimensions
partitioned_sizes = (
    self._partitioned_dim_sizes + tuple([
        self._inner_dim_sizes[i] for i in range(axis_in_inner_dims)
    ]) + (lengths,))
inner_sizes = self._inner_dim_sizes[axis_in_inner_dims + 1:]
exit(RaggedTensorDynamicShape(partitioned_sizes, inner_sizes))
