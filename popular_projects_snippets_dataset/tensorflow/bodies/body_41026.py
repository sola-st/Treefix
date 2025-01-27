# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Checks the python_function's args to be valid against input_signature."""
if self.input_signature is not None:
    arglen = len(self.input_signature)
    arg_names_len = len(self.arg_names)
    defaults = self.fullargspec.defaults or ()
    unbound_self_arg = 1 if (not self.is_method and arg_names_len > 0 and
                             self.arg_names[0] == "self") else 0
    if not all(d is BOUND_VALUE for d in defaults):
        default_arg_len = len(defaults)
        required_arg_len = arg_names_len - default_arg_len - unbound_self_arg
        # The input signature must cover all required function arguments.
        if arglen < required_arg_len:
            missing_tensor_specs = self.arg_names[arglen:required_arg_len]
            raise TypeError(
                f"The decorated tf.function has {required_arg_len} "
                f"required argument(s), but tf.function was only passed an "
                f"input_signature of length {arglen}. This covers {arglen} "
                f"required argument(s): {self.arg_names[:arglen]}, "
                f"but TensorSpecs are still required for the remaining "
                f"{len(missing_tensor_specs)} argument(s):"
                f" {missing_tensor_specs}.")
