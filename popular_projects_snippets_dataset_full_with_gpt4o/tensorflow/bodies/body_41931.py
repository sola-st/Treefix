# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns a string summarizing this function's structured signature.

    Args:
      default_values: If true, then include default values in the signature.

    Returns:
      A `string`.
    """
# Note: we can't just use self._funcion_spec.signature_summary(), because
# that would show "BOUND_VALUE" as the default value for all arguments.
assert self._function_spec is not None
arg_specs, kwarg_specs = self.structured_input_signature
arg_names = list(self._function_spec.arg_names)

# If an explicit input_signature is provided to @tf.function, then any
# arguments with defaults that are not covered by that explicit signature
# are simply dropped from the signature.
# TODO(b/159639913) Look into whether dropping arguments with default values
# from the signature is the right thing to do.
arg_names = arg_names[:len(arg_specs)]

if default_values:
    for i in range(len(arg_names)):
        if not _contains_type_spec(arg_specs[i]):
            arg_names[i] += "={}".format(arg_specs[i])
if kwarg_specs:
    arg_names.append("*")
    for name, spec in kwarg_specs.items():
        arg_names.append(name)
        if default_values and not _contains_type_spec(spec):
            arg_names[-1] += "={}".format(spec)
signature = f"{self._func_graph.name}({', '.join(arg_names)})"

exit(signature)
