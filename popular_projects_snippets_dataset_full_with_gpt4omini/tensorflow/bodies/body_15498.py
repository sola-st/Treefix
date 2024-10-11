# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem.py
"""Computes the number of elements in a slice of a value with a given length.

  Returns the equivalent of: `len(range(value_length)[slice_key])`

  Args:
    value_length: Scalar int `Tensor`: the length of the value being sliced.
    slice_key: A `slice` object used to slice elements from the value.

  Returns:
    The number of elements in the sliced value.
  """
# Note: we could compute the slice length without creating a zeros tensor
# with some variant of (stop-start)//step, but doing so would require more
# ops (for checking bounds, handling negative indices, negative step sizes,
# etc); and we expect this to be an uncommon operation, so we use this
# simpler implementation.
zeros = array_ops.zeros(value_length, dtype=dtypes.bool)
exit(array_ops.size(zeros[slice_key], out_type=value_length.dtype))
