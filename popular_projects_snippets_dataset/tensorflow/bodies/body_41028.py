# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Canonicalizes `args` and `kwargs`.

    Canonicalize the inputs to the Python function using a `FunctionSpec`
    instance. In particular, we parse the varargs and kwargs that the
    original function was called with into a tuple corresponding to the
    Python function's positional (named) arguments and a dictionary
    corresponding to its kwargs.  Missing default arguments are added.

    If this `FunctionSpec` has an input signature, then it is used to convert
    arguments to tensors; otherwise, any inputs containing numpy arrays are
    converted to tensors.

    Additionally, any inputs containing numpy arrays are converted to Tensors.

    Args:
      args: The varargs this object was called with.
      kwargs: The keyword args this function was called with.

    Returns:
      A canonicalized ordering of the inputs, as well as full and filtered
      (Tensors and Variables only) versions of their concatenated flattened
      representations, represented by a tuple in the form (args, kwargs,
      flat_args, filtered_flat_args). Here: `args` is a full list of bound
      arguments, and `kwargs` contains only true keyword arguments, as opposed
      to named arguments called in a keyword-like fashion.

    Raises:
      ValueError: If a keyword in `kwargs` cannot be matched with a positional
        argument when an input signature is specified, or when the inputs
        do not conform to the input signature.
    """
if self.is_pure:
    args, kwargs = _convert_variables_to_tensors(args, kwargs)
args, kwargs = self.bind_function_inputs(args, kwargs)
args, kwargs = cast_inputs(args, kwargs, self.input_signature)
filtered_flat_args = filter_function_inputs(args, kwargs)

exit((args, kwargs, filtered_flat_args))
