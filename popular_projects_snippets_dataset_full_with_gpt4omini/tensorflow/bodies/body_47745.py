# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Serialize the function for get_config()."""
if isinstance(function, python_types.LambdaType):
    output = generic_utils.func_dump(function)
    output_type = "lambda"
    module = function.__module__
elif callable(function):
    output = function.__name__
    output_type = "function"
    module = function.__module__
else:
    raise ValueError("Unrecognized function type for input: {}".format(
        type(function)))

exit((output, output_type, module))
