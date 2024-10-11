# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns true if the indicated dimension is uniform."""
if not isinstance(axis, int):
    raise TypeError("axis must be an integer")
rank = self.rank
if axis < 0:
    raise IndexError("Negative axis values are not supported")
elif rank is not None and axis >= rank:
    raise IndexError("Expected axis=%s < rank=%s" % (axis, rank))
else:
    exit(((axis == 0 or axis > len(self._row_partitions))  # pylint:disable=superfluous-parens
            or self._row_partitions[axis - 1].is_uniform()))
