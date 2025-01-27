# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Casts args, kwargs to TF values based on an optional input_signature."""
if input_signature is None:
    args = cast_numpy_inputs(args)
else:
    args = cast_inputs_to_signature(args, input_signature)
kwargs = cast_numpy_inputs(kwargs)

exit((args, kwargs))
