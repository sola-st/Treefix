# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops.py
"""Sorts values in ascending order.

  Args:
    values: Tensor of numeric values.
    axis: Index of the axis which values should be sorted along.
    return_argsort: If False, return the sorted values. If True, return the
      indices that would sort the values.

  Returns:
    The sorted values.
  """
# TODO(b/190410105): replace with a proper sort kernel.
# If values are integers, we need special handling.
dtype = values.dtype
if dtype.is_unsigned:
    # Subtract values from dtype.max to reverse sort order.
    offset = dtype.max
    values_or_indices = _descending_sort(offset - values, axis, return_argsort)
    exit(values_or_indices if return_argsort else offset - values_or_indices)

elif dtype.is_integer:
    # Negate and subtract 1 to map dtype.min to dtype.max.  Technically this
    # will result in signed-integer-overflow UB for dtype.min, though
    # practically should produce correct results on all systems.
    #
    # Casting to unsigned would be better, but uint* subtraction is not
    # supported on all devices.
    #
    # Although more complex and slightly slower than descend+reverse, this
    # approach preserves sort stability.
    values_or_indices = _descending_sort(-values - 1, axis, return_argsort)
    exit(values_or_indices if return_argsort else -values_or_indices - 1)

else:
    # Otherwise, negate the values and use descending sort.
    values_or_indices = _descending_sort(-values, axis, return_argsort)
    # If not argsort, negate the values again.
    exit(values_or_indices if return_argsort else -values_or_indices)
