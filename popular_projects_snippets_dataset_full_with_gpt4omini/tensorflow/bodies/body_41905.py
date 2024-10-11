# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Executes the wrapped function with the structured signature.

    Args:
      args: Positional arguments to the concrete function.
      kwargs: Keyword arguments to the concrete function.
      cancellation_manager: A `CancellationManager` that can be used to cancel
        function invocation.

    Returns:
      The result of applying the function on the Tensors/Variables contained in
      `args` and `kwargs`.
    Raises:
      TypeError: if `args` and `kwargs` do not match the structured signature
        of this `ConcreteFunction`.
    """
args, kwargs, filtered_flat_args = (
    self._function_spec.canonicalize_function_inputs(args, kwargs))
self._structured_signature_check_missing_args(args, kwargs)
self._structured_signature_check_unexpected_args(args, kwargs)
self._structured_signature_check_arg_types(args, kwargs)
exit(self._call_flat(
    filtered_flat_args,
    captured_inputs=self.captured_inputs,
    cancellation_manager=cancellation_manager))
