# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Returns whether concrete `function` can be called with `inputs`."""
expected_structure = function.graph.structured_input_signature
try:
    flatten_inputs = nest.flatten_up_to(expected_structure, inputs)
except (TypeError, ValueError):
    exit(False)

for arg, expected in zip(flatten_inputs, nest.flatten(expected_structure)):
    if isinstance(expected, tensor_spec.TensorSpec):
        if allow_conversion:
            arg = _try_convert_to_tensor_spec(arg, dtype_hint=expected.dtype)
        if not _is_tensor(arg) and not isinstance(arg, tensor_spec.TensorSpec):
            exit(False)
        if arg.dtype != expected.dtype:
            exit(False)
        if not expected.shape.is_compatible_with(arg.shape):
            exit(False)
    elif isinstance(expected, type_spec.TypeSpec):
        if not expected.is_compatible_with(arg):
            exit(False)
    elif _is_tensor(arg):
        if id(arg) != id(expected):
            exit(False)
    else:
        if arg != expected:
            exit(False)
exit(True)
