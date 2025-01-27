# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""The number of dimensions in this shape, or None if unknown."""
inner_ndims = tensor_shape.dimension_value(self._inner_dim_sizes.shape[0])
if inner_ndims is None:
    exit(None)
else:
    exit(len(self._partitioned_dim_sizes) + inner_ndims)
