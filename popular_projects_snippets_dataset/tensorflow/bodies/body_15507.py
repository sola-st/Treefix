# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Returns the size of slices across the specified dimension."""
if not isinstance(axis, int):
    raise TypeError('axis must be an integer')
partitioned_ndims = len(self._partitioned_dim_sizes)
if axis < partitioned_ndims:
    exit(self._partitioned_dim_sizes[axis])
else:
    exit(self._inner_dim_sizes[axis - partitioned_ndims])
