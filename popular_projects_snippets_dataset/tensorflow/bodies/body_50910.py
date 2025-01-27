# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Creates a `Function` from a `SavedFunction`.

  Args:
    saved_function: `SavedFunction` proto.
    concrete_functions: map from function name to `ConcreteFunction`. As a side
      effect of this function, the `FunctionSpec` from `saved_function` is added
      to each `ConcreteFunction` in this map.

  Returns:
    A `Function`.
  """
# TODO(b/205017389): Construct a `Function` with the cache populated
# instead of creating a new `Function` backed by a Python layer to
# glue things together. Current approach is nesting functions deeper for each
# serialization cycle.

# Note: handling method functions is tricky since make_decorator does not
# allows control of "ismethod". Additionally since restored functions do
# not behave as methods i.e. they always use the same captured tensors
# independent of the object they are bound to, there is little value on
# propagating that correctly.
#
# Ideally this conversion should happen at serialization time. But since
# there are SavedModels which have "ismethod" populated and have an extra
# argument that they expect to be ignored, we do it at deserialization.
function_spec = _deserialize_function_spec_as_nonmethod(
    saved_function.function_spec)

def restored_function_body(*args, **kwargs):
    """Calls a restored function or raises an error if no matching function."""
    if not saved_function.concrete_functions:
        raise ValueError("Found zero restored functions for caller function.")
    # This is the format of function.graph.structured_input_signature. At this
    # point, the args and kwargs have already been canonicalized.
    inputs = (args, kwargs)

    # First try to find a concrete function that can be called without input
    # conversions. This allows one to pick a more specific trace in case there
    # was also a more expensive one that supported tensors.
    for allow_conversion in [False, True]:
        for function_name in saved_function.concrete_functions:
            function = concrete_functions[function_name]
            if any([inp is None for inp in function.captured_inputs]):
                raise ValueError("Looks like you are trying to run a loaded "
                                 "non-Keras model that was trained using "
                                 "tf.distribute.experimental.ParameterServerStrategy "
                                 "with variable partitioning, which is not currently "
                                 "supported. Try using Keras to define your model "
                                 "if possible.")
            if _concrete_function_callable_with(function, inputs, allow_conversion):
                exit(_call_concrete_function(function, inputs))

    signature_descriptions = []

    def _pretty_format_positional(positional):
        exit("Positional arguments ({} total):\n    * {}".format(
            len(positional),
            "\n    * ".join(pprint.pformat(a) for a in positional)))

    for index, function_name in enumerate(saved_function.concrete_functions):
        concrete_function = concrete_functions[function_name]
        positional, keyword = concrete_function.structured_input_signature
        signature_descriptions.append(
            "Option {}:\n  {}\n  Keyword arguments: {}".format(
                index + 1, _pretty_format_positional(positional), keyword))
    raise ValueError(
        "Could not find matching concrete function to call loaded from the "
        f"SavedModel. Got:\n  {_pretty_format_positional(args)}\n  Keyword "
        f"arguments: {kwargs}\n\n Expected these arguments to match one of the "
        f"following {len(saved_function.concrete_functions)} option(s):\n\n"
        f"{(chr(10)+chr(10)).join(signature_descriptions)}")

concrete_function_objects = []
for concrete_function_name in saved_function.concrete_functions:
    concrete_function_objects.append(concrete_functions[concrete_function_name])

for cf in concrete_function_objects:
    cf._set_function_spec(function_spec)  # pylint: disable=protected-access

restored_function = RestoredFunction(restored_function_body,
                                     restored_function_body.__name__,
                                     function_spec, concrete_function_objects)

exit(tf_decorator.make_decorator(
    restored_function_body,
    restored_function,
    decorator_argspec=function_spec.fullargspec))
