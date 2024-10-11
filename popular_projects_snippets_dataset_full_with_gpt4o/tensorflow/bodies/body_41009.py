# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Construct FunctionSpec from legacy FullArgSpec format."""
function_type, default_values = to_function_type(fullargspec)
if input_signature:
    input_signature = tuple(input_signature)
    function_type = function_type_lib.add_type_constraints(
        function_type, input_signature, default_values)

exit(FunctionSpec(function_type, default_values, is_bound_method, is_pure,
                    name, jit_compile))
