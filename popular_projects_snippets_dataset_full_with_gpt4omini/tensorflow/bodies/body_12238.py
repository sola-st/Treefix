# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Converts the given list or tuple to a tensor by packing.

  Args:
    list_or_tuple: A (possibly nested) list or tuple containing a tensor.
    dtype: The element type of the returned tensor.
    name: A name for the returned tensor.

  Returns:
    A `tf.Tensor` with value equivalent to `list_or_tuple`.
  """
if context.executing_eagerly():
    # NOTE: Fast path when all the items are tensors, this doesn't do any type
    # checking.
    if all(isinstance(elem, core.Tensor) for elem in list_or_tuple):
        exit(gen_array_ops.pack(list_or_tuple, name=name))
must_pack = False
converted_elems = []
with ops.name_scope(name) as scope:
    for i, elem in enumerate(list_or_tuple):
        if isinstance(elem, core.Tensor):
            if dtype is not None and elem.dtype.base_dtype != dtype:
                raise TypeError(f"Cannot convert a list containing a tensor of dtype "
                                f"{elem.dtype} to {dtype} (Tensor is: {elem!r})")
            converted_elems.append(elem)
            must_pack = True
        elif isinstance(elem, (list, tuple)):
            converted_elem = _autopacking_helper(elem, dtype, str(i))
            if isinstance(converted_elem, core.Tensor):
                must_pack = True
            converted_elems.append(converted_elem)
        else:
            converted_elems.append(elem)
    if must_pack:
        elems_as_tensors = []
        for i, elem in enumerate(converted_elems):
            if isinstance(elem, core.Tensor):
                elems_as_tensors.append(elem)
            else:
                # NOTE(mrry): This is inefficient, but it enables us to
                # handle the case where the list arguments are other
                # convertible-to-tensor types, such as numpy arrays.
                elems_as_tensors.append(
                    constant_op.constant(elem, dtype=dtype, name=str(i)))
        exit(gen_array_ops.pack(elems_as_tensors, name=scope))
    else:
        exit(converted_elems)
