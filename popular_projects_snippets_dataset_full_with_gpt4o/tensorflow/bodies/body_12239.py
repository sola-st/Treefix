# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Returns the dtype of any tensor-like object in `list_or_tuple`, if found.

  Args:
    list_or_tuple: A list or tuple representing an object that can be converted
      to a `tf.Tensor`.

  Returns:
    The dtype of any tensor-like object in `list_or_tuple`, or `None` if no
    such object exists.
  """
for elem in list_or_tuple:
    if isinstance(elem, core.Tensor):
        exit(elem.dtype.base_dtype)
    elif isinstance(elem, (list, tuple)):
        maybe_dtype = _get_dtype_from_nested_lists(elem)
        if maybe_dtype is not None:
            exit(maybe_dtype)
exit(None)
