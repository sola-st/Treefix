# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Raise TypeError if `arg`'s type doesn't match `spec`."""
if arg is function_spec.BOUND_VALUE:
    exit()

# TODO(xjun): Expand this to all CompositeTensors after removing
# TraceType.Reference usage from IteratorSpec.
if isinstance(arg, resource_variable_ops.BaseResourceVariable):
    arg_spec = trace_type.from_value(arg, signature_context)
else:
    arg_spec = arg

# Check the overall nested structure of the argument.
try:
    nest.assert_same_structure(arg_spec, spec, expand_composites=True)
except (ValueError, TypeError):
    try:
        nest.assert_same_structure(arg_spec, spec, expand_composites=False)
        expected, got = spec, arg_spec
    except (ValueError, TypeError):
        expected, got = _structure_summary(spec), _structure_summary(arg_spec)
    raise TypeError(f"{self._structured_signature_summary()}: argument "
                    f"{name} had incorrect type\n"
                    f"  expected: {expected}\n"
                    f"       got: {got}")

# Check the type for each leaf in the nested structure.
arg_pieces = nest.flatten(arg, expand_composites=True)
spec_pieces = nest.flatten(spec, expand_composites=True)
for (arg_piece, spec_piece) in zip(arg_pieces, spec_pieces):
    # TODO(mdan): Use consistent error messages.
    if isinstance(spec_piece, tensor_spec.DenseSpec):
        # TODO(edloper): Consider calling convert_to_tensor on non-tensor
        # values here.  That would match the behavior of
        # _call_concrete_function() in function_deserialization.py.  If
        # we do, then we need to change the nest assert_same_structure and
        # flatten calls above to use shallow variants.
        tensor_types = (ops.Tensor, resource_variable_ops.BaseResourceVariable)
        if not isinstance(arg_piece, tensor_types):
            raise TypeError(f"{self._structured_signature_summary()} expected a "
                            f"Tensor in {name}, but got "
                            f"{type(arg_piece).__name__} value {arg_piece}.")
    elif arg_piece is not function_spec.BOUND_VALUE:
        try:
            arg_matches_spec = bool(arg_piece == spec_piece)
        except (ValueError, TypeError):
            logging.vlog(1, "Error matching value with spec", exc_info=True)
            arg_matches_spec = False
        if not arg_matches_spec:
            raise TypeError(
                f"ConcreteFunction {self._structured_signature_summary()} was "
                f"constructed with {type(spec_piece).__name__} value "
                f"{spec_piece} in {name}, but was called with "
                f"{type(arg_piece).__name__} value {arg_piece}.")
