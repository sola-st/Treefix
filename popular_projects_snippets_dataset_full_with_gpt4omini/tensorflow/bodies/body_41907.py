# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Raises a TypeError if there are any extra args."""
arg_specs, kwarg_specs = self.structured_input_signature
if len(args) > len(arg_specs):
    raise TypeError(
        f"{self._structured_signature_summary()} takes "
        f"{len(self._function_spec.arg_names)} positional arguments but got "
        f"{len(args)}.")
if len(kwargs) > len(kwarg_specs):
    extra_args = set(kwargs) - set(kwarg_specs)
    raise TypeError(f"{self._structured_signature_summary()} got unexpected "
                    f"keyword arguments: {', '.join(extra_args)}.")
