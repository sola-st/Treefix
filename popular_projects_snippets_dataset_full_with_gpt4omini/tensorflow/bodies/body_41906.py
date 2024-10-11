# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Raises a TypeError if any args are missing."""
arg_specs, kwarg_specs = self.structured_input_signature
missing_arguments = []
for i, (arg, spec) in enumerate(zip(args, arg_specs)):
    if arg is function_spec.BOUND_VALUE and _contains_type_spec(spec):
        missing_arguments.append(self._function_spec.arg_names[i])
for (name, arg) in kwargs.items():
    if arg is function_spec.BOUND_VALUE and _contains_type_spec(
        kwarg_specs[name]):
        missing_arguments.append(name)
if missing_arguments:
    raise TypeError(f"{self._structured_signature_summary()} missing "
                    "required arguments: "
                    f"{', '.join(sorted(missing_arguments))}.")
