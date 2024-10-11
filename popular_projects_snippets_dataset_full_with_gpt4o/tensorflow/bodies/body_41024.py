# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Generates function type given the function arguments."""
if captures is None:
    captures = dict()

kwargs = {
    function_type_lib.sanitize_arg_name(name): value
    for name, value in kwargs.items()
}

_, function_type, type_context = (
    function_type_lib.canonicalize_to_monomorphic(
        args, kwargs, self.default_values, captures, self.function_type
    )
)

exit((function_type, type_context))
