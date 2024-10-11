# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Executes the wrapped function with the flat signature.

    Args:
      args: Positional arguments to the concrete function.
      kwargs: Keyword arguments to the concrete function.
      cancellation_manager: A `CancellationManager` that can be used to cancel
        function invocation.

    Returns:
      The result of applying the function on the Tensors/Variables contained in
      `args` and `kwargs`.
    Raises:
      TypeError: if `args` and `kwargs` do not match the flat signature of this
        `ConcreteFunction`.
    """
if len(args) > self._num_positional_args:
    raise TypeError(
        f"{self._flat_signature_summary()} takes {self._num_positional_args} "
        f"positional arguments, got {len(args)}.")
args = list(args)
kwargs = dict(kwargs)
kwargs = {
    function_type_lib.sanitize_arg_name(k): v for k, v in kwargs.items()
}
for keyword in self._arg_keywords[len(args):]:
    try:
        args.append(
            kwargs.pop(
                function_type_lib.sanitize_arg_name(compat.as_str(keyword))))
    except KeyError:
        specified_keywords = (
            list(self._arg_keywords[:len(args)]) + list(kwargs.keys()))
        missing_required_args = sorted(
            set(self._arg_keywords) - set(specified_keywords))
        raise TypeError(f"{self._flat_signature_summary()} missing required "
                        f"arguments: {', '.join(missing_required_args)}.")
if kwargs:
    positional_arg_keywords = set(self._arg_keywords[:len(args)])
    for unused_key in kwargs:
        if unused_key in positional_arg_keywords:
            raise TypeError(f"{self._flat_signature_summary()} got two values "
                            f"for '{unused_key}'.")
    raise TypeError(f"{self._flat_signature_summary()} got unexpected "
                    f"keyword arguments: {', '.join(sorted(kwargs))}.")

for i, arg in enumerate(args):
    if not isinstance(
        arg, (ops.Tensor, resource_variable_ops.BaseResourceVariable)):
        raise TypeError(f"{self._flat_signature_summary()}: expected argument "
                        f"#{i}(zero-based) to be a Tensor; "
                        f"got {type(arg).__name__} ({arg}).")
exit(self._call_flat(args, self.captured_inputs, cancellation_manager))
