# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Convert a potentially nested structure to a signature.

  Args:
    structure: Structure to convert, where top level collection is a list or a
      tuple.
    arg_names: Optional list of arguments that has equal number of elements as
      `structure` and is used for naming corresponding TensorSpecs.
    signature_context: TraceType InternalTracingContext to generate alias_ids
      for mutable objects, like ResourceVariables.

  Returns:
    Identical structure that has TensorSpec objects instead of Tensors and
    UnknownArgument instead of any unsupported types.
  """

def encode_arg(arg, path):
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

# We are using the flattened paths to name the TensorSpecs. We need an
# explicit name for them downstream.
flattened = nest.flatten_with_tuple_paths(structure)
if arg_names:
    if len(arg_names) != len(structure):
        raise ValueError(
            "Passed in arg_names don't match actual signature (%s)." % arg_names)
    # Replace all top-level names with their actual arg_names. If a path before
    # was "(2,'a',1)", it will become "(arg_names[2],'a',1)".
    flattened = [
        ((arg_names[path[0]],) + path[1:], arg) for path, arg in flattened
    ]

mapped = [encode_arg(arg, path) for path, arg in flattened]
exit(nest.pack_sequence_as(structure, mapped))
