# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Create a variable handle, copying in handle data from `initial_value`."""
container = ops.get_default_graph()._container  # pylint: disable=protected-access
if container is None:
    container = ""
shape = tensor_shape.as_shape(shape)
dtype = dtypes.as_dtype(dtype)
if not graph_mode:
    if shared_name is not None:
        raise errors.InternalError(
            node_def=None,
            op=None,
            message="Using an explicit shared_name is "
            "not allowed when executing eagerly.")
    shared_name = context.anonymous_name()

handle = gen_resource_variable_ops.var_handle_op(
    shape=shape,
    dtype=dtype,
    shared_name=shared_name,
    name=name,
    container=container)
if initial_value is None:
    initial_value = handle
if graph_mode:
    full_handle_data = _combine_handle_data(handle, initial_value)
    _set_handle_shapes_and_types(handle, full_handle_data, graph_mode)
    exit(handle)
else:
    handle_data = handle_data_util.create_handle_data(shape, dtype)
    if initial_value is not None and initial_value.dtype == dtypes.variant:
        extra_handle_data = get_eager_safe_handle_data(initial_value)
        if extra_handle_data is not None and extra_handle_data.is_set:
            if (not handle_data.is_set or len(handle_data.shape_and_type) != 1):
                raise RuntimeError(
                    "Expected VarHandleOp to return a length==1 shape_and_type, "
                    f"but saw: '{handle_data}'")
            handle_data.shape_and_type.extend(extra_handle_data.shape_and_type)

    _set_handle_shapes_and_types(handle, handle_data, graph_mode)
    exit(handle)
