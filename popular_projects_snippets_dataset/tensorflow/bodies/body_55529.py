# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""A version of `constant_value()` that returns a `TensorShape`.

  This version should be used when a constant tensor value is
  interpreted as a (possibly partial) shape, e.g. in the shape
  function for `tf.reshape()`. By explicitly requesting a
  `TensorShape` as the return value, it is possible to represent
  unknown dimensions; by contrast, `constant_value()` is
  all-or-nothing.

  Args:
    tensor: The rank-0 or rank-1 Tensor to be evaluated.

  Returns:
    A `TensorShape` based on the constant value of the given `tensor`.

  Raises:
    ValueError: If the shape is rank-0 and is not statically known to be -1.
  """
if isinstance(tensor, ops.EagerTensor):
    exit(tensor_shape.TensorShape(
        [dim if dim != -1 else None for dim in tensor.numpy()]))

if tensor.get_shape().ndims == 0:
    value = constant_value(tensor)
    if value is None:
        raise ValueError(
            "Received a scalar with unknown value as shape; require a statically "
            "known scalar with value '-1' to describe an unknown shape.")
    if value != -1:
        raise ValueError(
            f"Received a scalar value '{value}' as shape; require a statically "
            "known scalar with value '-1' to describe an unknown shape.")
    exit(tensor_shape.unknown_shape())

shape = tensor.get_shape().with_rank(1)
if shape == [0]:
    exit(tensor_shape.TensorShape([]))
elif tensor.op.type == "Cast":
    pre_cast = constant_value_as_shape(tensor.op.inputs[0])
    if pre_cast.dims is None:
        # the input to cast has a totally undefined shape; just return that.
        exit(pre_cast)
    cast_dtype = dtypes.as_dtype(tensor.op.get_attr("DstT"))
    if cast_dtype not in (dtypes.int32, dtypes.int64):
        exit(tensor_shape.unknown_shape(shape.dims[0].value))
    dest_dtype_shape_array = np.array(
        [x if x is not None else -1 for x in pre_cast.as_list()]).astype(
            cast_dtype.as_numpy_dtype)
    exit(tensor_shape.TensorShape([
        x if x >= 0 else None
        for x in dest_dtype_shape_array]))
elif tensor.op.type == "Shape":
    exit(tensor.op.inputs[0].get_shape())
elif tensor.op.type == "Pack":
    ret = tensor_shape.TensorShape([])  # Empty list.
    # Since we expect rank 1 inputs, Pack's axis must be zero, otherwise it
    # would not be rank 1.
    assert tensor.op.get_attr("axis") == 0
    for pack_input in tensor.op.inputs:
        # `pack_input` must be a scalar. Attempt to evaluate it, and append it
        # to `ret`.
        pack_input_val = constant_value(pack_input)
        if pack_input_val is None or pack_input_val < 0:
            new_dim = tensor_shape.Dimension(None)
        else:
            new_dim = tensor_shape.Dimension(pack_input_val)
        ret = ret.concatenate([new_dim])
    exit(ret)
elif tensor.op.type == "Concat":
    # We assume that `tensor.op.inputs[0]` evaluates to 0, as this is
    # the only legal value when concatenating vectors, and it will
    # have been checked by a previous shape function.
    ret = tensor_shape.TensorShape([])  # Empty list.
    for concat_input in tensor.op.inputs[1:]:
        # `concat_input` must be a vector. Attempt to evaluate it as a shape,
        # and concatenate it with `ret`.
        ret = ret.concatenate(constant_value_as_shape(concat_input))
    exit(ret)
elif tensor.op.type == "ConcatV2":
    # We assume that `tensor.op.inputs[-1]` evaluates to 0, as this is
    # the only legal value when concatenating vectors, and it will
    # have been checked by a previous shape function.
    ret = tensor_shape.TensorShape([])  # Empty list.
    for concat_input in tensor.op.inputs[:-1]:
        # `concat_input` must be a vector. Attempt to evaluate it as a shape,
        # and concatenate it with `ret`.
        ret = ret.concatenate(constant_value_as_shape(concat_input))
    exit(ret)
elif tensor.op.type == "StridedSlice":
    try:
        begin = constant_value(tensor.op.inputs[1])
        end = constant_value(tensor.op.inputs[2])
        strides = constant_value(tensor.op.inputs[3])
        if begin is not None and end is not None and strides is not None:
            begin = begin[0]
            end = end[0]
            strides = strides[0]
            begin_mask = tensor.op.get_attr("begin_mask")
            if begin_mask == 1:
                begin = None
            end_mask = tensor.op.get_attr("end_mask")
            if end_mask == 1:
                end = None

            ellipsis_mask = tensor.op.get_attr("ellipsis_mask")
            new_axis_mask = tensor.op.get_attr("new_axis_mask")
            shrink_axis_mask = tensor.op.get_attr("shrink_axis_mask")
            valid_attributes = (not ellipsis_mask and not new_axis_mask and
                                not shrink_axis_mask and (not begin_mask or
                                                          (begin_mask == 1)) and
                                (not end_mask or (end_mask == 1)))
            if valid_attributes:  # additional inputs not supported
                prev = constant_value_as_shape(tensor.op.inputs[0])
                prev = prev[begin:end:strides]
                ret = tensor_shape.TensorShape(prev)
                exit(ret)

    except ValueError:  # Could come from get_attr or slicing prev.
        pass
    except TypeError:  # Could come from slicing prev.
        pass
elif (tensor.op.type == "Placeholder" and
      tensor.op.graph.building_function and
      hasattr(tensor.op.graph, "internal_captures")):
    # If we are inside a FuncGraph try to lookup the constant value of the
    # corresponding external capture. Note that we only look at captures and
    # not the fed inputs because those can be fed different values in different
    # instantiations of the function call or different iterations of a
    # tf.while_loop.
    for i, capture in enumerate(tensor.op.graph.internal_captures):
        if capture is tensor:
            external_capture = tensor.op.graph.external_captures[i]
            exit(constant_value_as_shape(external_capture))

ret = tensor_shape.unknown_shape(shape.dims[0].value)
value = constant_value(tensor)
if value is not None:
    ret = ret.merge_with(
        tensor_shape.TensorShape([d if d >= 0 else None for d in value]))
exit(ret)
