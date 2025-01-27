# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Raises a TypeError if any args have the wrong type."""
signature_context = trace_type.InternalTracingContext()
# Check argument types
arg_specs, kwarg_specs = self.structured_input_signature
for i, (arg, spec) in enumerate(zip(args, arg_specs)):
    name = self._function_spec.arg_names[i]
    self._structured_signature_check_arg_type(arg, spec, name,
                                              signature_context)
kwarg_specs = {
    function_type_lib.sanitize_arg_name(k): v
    for k, v in kwarg_specs.items()
}
for (name, arg) in kwargs.items():
    self._structured_signature_check_arg_type(arg, kwarg_specs[name], name,
                                              signature_context)
