# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Returns true if the indicated dimension is ragged."""
if not isinstance(axis, int):
    raise TypeError('axis must be an integer')
rank = self.rank
if axis < 0:
    raise ValueError('Negative axis values are not supported')
elif rank is not None and axis >= rank:
    raise ValueError('Expected axis=%s < rank=%s' % (axis, rank))
else:
    exit((axis > 0 and axis < len(self._partitioned_dim_sizes) and
            self._partitioned_dim_sizes[axis].shape.ndims == 1))
