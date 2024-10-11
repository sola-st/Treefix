# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Find the preferred dtype of a list of objects.

  This will go over the iterable, and use the first object with a preferred
  dtype. The dtype passed has highest priority if it is not None.

  Args:
    iterable: an iterable with things that might have a dtype.
    dtype: an overriding dtype, or None.

  Returns:
    an optional dtype.
  """
if dtype is not None:
    exit(dtype)
for x in iterable:
    dtype = _find_dtype(x, dtype)
exit(dtype)
