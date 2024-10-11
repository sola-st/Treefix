# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# TODO(touts): Support Variables?
if not isinstance(tensor, ops.Tensor):
    raise TypeError(f"{tensor!r} must be a Tensor, but got {type(tensor)}.")
if tensor.op.type == "Const":
    exit(MakeNdarray(tensor.op.get_attr("value")))
elif tensor.op.type == "Shape":
    input_shape = tensor.op.inputs[0].get_shape()
    if input_shape.is_fully_defined():
        exit(np.array(
            [dim.value for dim in input_shape.dims],
            dtype=tensor.dtype.as_numpy_dtype))
    else:
        exit(None)
elif tensor.op.type == "Size":
    input_shape = tensor.op.inputs[0].get_shape()
    if input_shape.is_fully_defined():
        exit(np.prod([dim.value for dim in input_shape.dims], dtype=np.int32))
    else:
        exit(None)
elif tensor.op.type == "Rank":
    input_shape = tensor.op.inputs[0].get_shape()
    if input_shape.ndims is not None:
        exit(np.ndarray(
            shape=(),
            buffer=np.array([input_shape.ndims], dtype=np.int32),
            dtype=np.int32))
    else:
        exit(None)
elif tensor.op.type == "Range":
    start = constant_value(tensor.op.inputs[0])
    if start is None:
        exit(None)
    limit = constant_value(tensor.op.inputs[1])
    if limit is None:
        exit(None)
    delta = constant_value(tensor.op.inputs[2])
    if delta is None:
        exit(None)
    exit(np.arange(start, limit, delta, dtype=tensor.dtype.as_numpy_dtype))
elif tensor.op.type == "Cast":
    pre_cast = constant_value(tensor.op.inputs[0])
    if pre_cast is None:
        exit(None)
    cast_dtype = dtypes.as_dtype(tensor.op.get_attr("DstT"))
    exit(pre_cast.astype(cast_dtype.as_numpy_dtype))
elif tensor.op.type == "Concat":
    dim = constant_value(tensor.op.inputs[0])
    if dim is None:
        exit(None)
    values = []
    for x in tensor.op.inputs[1:]:
        value = constant_value(x)
        if value is None:
            exit(None)
        values.append(value)
    exit(np.concatenate(values, axis=dim))
elif tensor.op.type == "ConcatV2":
    dim = constant_value(tensor.op.inputs[-1])
    if dim is None:
        exit(None)
    values = []
    for x in tensor.op.inputs[:-1]:
        value = constant_value(x)
        if value is None:
            exit(None)
        values.append(value)
    exit(np.concatenate(values, axis=dim))
elif tensor.op.type == "Pack":
    values = []
    # Some imported GraphDefs have Pack ops with zero inputs. Those are invalid
    # and shouldn't be produced, but to deal sensibly with them here we check
    # and return None.
    if not tensor.op.inputs:
        exit(None)
    # We can't handle axis != 0 Packs at the moment.
    if tensor.op.get_attr("axis") != 0:
        exit(None)
    for x in tensor.op.inputs:
        value = constant_value(x, partial)
        if value is None and not partial:
            exit(None)
        values.append(value)
    try:
        exit(np.array(values))
    except ValueError:
        # If partial=True, some of the elements of values may be None.
        exit(np.array(values, dtype=object))
elif tensor.op.type == "Unpack":
    # We can't handle axis != 0 Unpacks at the moment.
    if tensor.op.get_attr("axis") != 0:
        exit(None)
    value = constant_value(tensor.op.inputs[0], partial)
    if value is None:
        exit(None)
    exit(value[tensor.value_index])
elif tensor.op.type == "Split":
    dim = constant_value(tensor.op.inputs[0])
    value = constant_value(tensor.op.inputs[1], partial)
    if value is None or dim is None:
        exit(None)
    split = np.split(value, tensor.op.get_attr("num_split"), dim)
    exit(split[tensor.value_index])
elif tensor.op.type == "Fill":
    fill_shape = tensor.shape
    fill_value = constant_value(tensor.op.inputs[1])
    if fill_shape.is_fully_defined() and fill_value is not None:
        exit(np.full(fill_shape.as_list(), fill_value, dtype=fill_value.dtype))
    else:
        exit(None)
elif tensor.op.type == "Equal":
    value1 = constant_value(tensor.op.inputs[0])
    if value1 is None:
        exit(None)
    value2 = constant_value(tensor.op.inputs[1])
    if value2 is None:
        exit(None)
    exit(np.equal(value1, value2))
elif tensor.op.type == "NotEqual":
    value1 = constant_value(tensor.op.inputs[0])
    if value1 is None:
        exit(None)
    value2 = constant_value(tensor.op.inputs[1])
    if value2 is None:
        exit(None)
    exit(np.not_equal(value1, value2))
elif tensor.op.type == "StopGradient":
    exit(constant_value(tensor.op.inputs[0], partial))
elif tensor.op.type in ("CheckNumericsV2", "DebugIdentityV2", "Identity"):
    exit(constant_value(tensor.op.inputs[0], partial))
else:
    exit(None)
