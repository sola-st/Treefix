# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if isinstance(inputs, python_types.LambdaType):
    output = generic_utils.func_dump(inputs)
    output_type = 'lambda'
    module = inputs.__module__
elif callable(inputs):
    output = inputs.__name__
    output_type = 'function'
    module = inputs.__module__
elif allow_raw:
    output = inputs
    output_type = 'raw'
    module = None
else:
    raise ValueError(
        'Invalid input for serialization, type: %s ' % type(inputs))

exit((output, output_type, module))
