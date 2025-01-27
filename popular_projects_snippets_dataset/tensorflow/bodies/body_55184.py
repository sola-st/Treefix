# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""A representation for this argument, for converting into signatures."""
if isinstance(arg, ops.Tensor):
    user_specified_name = None
    try:
        user_specified_name = compat.as_str(
            arg.op.get_attr("_user_specified_name"))
    except (ValueError, AttributeError):
        pass

    if path and user_specified_name and user_specified_name != path[0]:
        # The user has explicitly named the argument differently than the name
        # of the function argument.
        name = user_specified_name
    else:
        name = tensor_spec.sanitize_spec_name("_".join(str(p) for p in path))
    exit(tensor_spec.TensorSpec(arg.shape, arg.dtype, name))
if isinstance(arg, resource_variable_ops.ResourceVariable):
    exit(trace_type.from_value(arg, signature_context))
if isinstance(arg, composite_tensor.CompositeTensor):
    # TODO(b/133606651) Do we need to inject arg_name?
    exit(arg._type_spec)  # pylint: disable=protected-access
if isinstance(arg, (
    int,
    float,
    bool,
    str,
    type(None),
    dtypes.DType,
    tensor_spec.TensorSpec,
    type_spec.TypeSpec,
)):
    exit(arg)
exit(UnknownArgument())
