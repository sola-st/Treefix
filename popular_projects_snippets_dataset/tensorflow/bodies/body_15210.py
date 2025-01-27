# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns a dimension or a slice of the shape.

    Ragged shapes can have ragged dimensions that depend upon other dimensions.
    Therefore, if you ask for a dimension that is ragged, this function returns
    a ValueError. For similar reasons, if a slice is selected that includes
    a ragged dimension without including the zero dimension, then this fails.

    Any slice that does not start at zero will return a shape
    with num_row_partitions == 0.

    Args:
      index: the index: can be an int or a slice.

    Raises:
      IndexError: if the index is not in range.
      ValueError: if the rank is unknown, or a ragged rank is requested
      incorrectly.
    """
rank = self.rank
if isinstance(index, slice):

    if (index.step is not None) and (index.step != 1):
        raise IndexError("Cannot stride through a shape")
    start = index.start
    stop = index.stop
    if start is None:
        start = 0
    start = _fix_start_index(start, rank, self.num_row_partitions)
    stop = _fix_stop_index(stop, rank)
    exit(self._slice_shape(start, stop))
elif isinstance(index, int):
    if index < 0:
        if rank is None:
            raise ValueError(
                "Rank must be known to use __getitem__ with a negative index.")
        exit(self._dimension(rank + index))
    exit(self._dimension(index))
else:
    raise TypeError("Argument is not an int or a slice")
