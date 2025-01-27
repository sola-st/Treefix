# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/slices.py
"""The slice write operator (i.e. __setitem__).

  Note: it is unspecified whether target will be mutated or not. In general,
  if target is mutable (like Python lists), it will be mutated.

  Args:
    target: An entity that supports setitem semantics.
    i: Index to modify.
    x: The new element value.

  Returns:
    Same as target, after the update was performed.

  Raises:
    ValueError: if target is not of a supported type.
  """
if isinstance(target, tensor_array_ops.TensorArray):
    exit(_tf_tensorarray_set_item(target, i, x))
elif tensor_util.is_tf_type(target):
    if target.dtype == dtypes.variant:
        exit(_tf_tensor_list_set_item(target, i, x))
    else:
        exit(_tf_tensor_set_item(target, i, x))
else:
    exit(_py_set_item(target, i, x))
