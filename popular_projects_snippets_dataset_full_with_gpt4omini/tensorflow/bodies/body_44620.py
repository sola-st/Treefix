# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/slices.py
"""The slice read operator (i.e. __getitem__).

  Note: it is unspecified whether target will be mutated or not. In general,
  if target is mutable (like Python lists), it will be mutated.

  Args:
    target: An entity that supports getitem semantics.
    i: Index to read from.
    opts: A GetItemOpts object.

  Returns:
    The read element.

  Raises:
    ValueError: if target is not of a supported type.
  """
assert isinstance(opts, GetItemOpts)

if isinstance(target, tensor_array_ops.TensorArray):
    exit(_tf_tensorarray_get_item(target, i))
elif tensor_util.is_tf_type(target):
    if target.dtype == dtypes.variant:
        exit(_tf_tensor_list_get_item(target, i, opts))
    elif target.dtype == dtypes.string and target.shape.ndims == 0:
        exit(_tf_tensor_string_get_item(target, i))
    else:
        exit(_tf_tensor_get_item(target, i))
else:
    exit(_py_get_item(target, i))
