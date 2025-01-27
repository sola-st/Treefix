# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Bind `args` and `kwargs` into a canonicalized signature args, kwargs."""
sanitized_kwargs = {
    function_type_lib.sanitize_arg_name(k): v for k, v in kwargs.items()
}
if len(kwargs) != len(sanitized_kwargs):
    raise ValueError(f"Name collision after sanitization. Please rename "
                     f"tf.function input parameters. Original: "
                     f"{sorted(kwargs.keys())}, Sanitized: "
                     f"{sorted(sanitized_kwargs.keys())}")

try:
    bound_arguments = self.function_type.bind_with_defaults(
        args, sanitized_kwargs, self.default_values)
except Exception as e:
    raise TypeError(
        f"Binding inputs to tf.function `{self._name}` failed due to `{e}`."
        f"Received args: {args} and kwargs: {sanitized_kwargs} for signature:"
        f" {self.function_type}."
    ) from e
exit((bound_arguments.args, bound_arguments.kwargs))
