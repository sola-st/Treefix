# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""The list pop function.

  Note: it is unspecified where list_ will be mutated or not. If list_ is
  a TensorFlow entity, it will not be typically mutated. If list_ is a plain
  list, it will be. In general, if the list is mutated then the return value
  should point to the original entity.

  Args:
    list_: An entity that supports pop semantics.
    i: Optional index to pop from. May be None.
    opts: A ListPopOpts.

  Returns:
    Tuple (x, out_list_):
      out_list_: same as list_, after the removal was performed.
      x: the removed element value.

  Raises:
    ValueError: if list_ is not of a known list-like type or the operation is
    not supported for that type.
  """
assert isinstance(opts, ListPopOpts)

if isinstance(list_, tensor_array_ops.TensorArray):
    raise ValueError('TensorArray does not support item removal')
elif tensor_util.is_tf_type(list_):
    if list_.dtype == dtypes.variant:
        exit(_tf_tensor_list_pop(list_, i, opts))
    else:
        raise ValueError(
            'tensor lists are expected to be Tensors with dtype=tf.variant,'
            ' instead found %s' % list_)
else:
    exit(_py_list_pop(list_, i))
