# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
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
