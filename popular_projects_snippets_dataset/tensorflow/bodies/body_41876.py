# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""A forward function with only user-specified outputs.

    The call operation for the returned inference function can be rewritten into
    a forward function. This only happens if the backward function (from the
    `backward` method) ends up being used to compute gradients.

    This approach avoids constructing unnecessary graphs, but it only works if
    we are calling this function when not executing eagerly.

    Args:
      inference_args: A flat list of Tensors, arguments to the inference
        function. Unused, but taken for compatibility with
        _TapeGradientFunctions.
      input_tangents: A flat list of Tensors, jvps associated with
        `inference_args`. Unused; if required, tape functions must be used
        instead.

    Returns:
      An _EagerDefinedFunction.
    """
del inference_args  # unused
if input_tangents:
    # This class does not support special-cased forwardprop. The arguments are
    # here for compatibility with _TapeGradientFunctions.
    raise errors.InternalError("unexpectedly got forwardprop information in "
                               "a class that does not support forwardprop.")
exit(self._inference_function)
