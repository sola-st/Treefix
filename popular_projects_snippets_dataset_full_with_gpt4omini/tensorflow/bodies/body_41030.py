# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Checks the input_signature to be valid."""
if signature is None:
    exit()

if not isinstance(signature, (tuple, list)):
    raise TypeError("input_signature must be either a tuple or a list, got "
                    f"{type(signature)}.")

# TODO(xjun): Allow VariableSpec once we figure out API for de-aliasing.
variable_specs = _get_variable_specs(signature)
if variable_specs:
    raise TypeError(
        f"input_signature doesn't support VariableSpec, got {variable_specs}")

if any(not isinstance(arg, tensor_spec.TensorSpec)
       for arg in nest.flatten(signature, expand_composites=True)):
    bad_args = [
        arg for arg in nest.flatten(signature, expand_composites=True)
        if not isinstance(arg, tensor_spec.TensorSpec)
    ]
    raise TypeError("input_signature must be a possibly nested sequence of "
                    f"TensorSpec objects, got invalid args {bad_args} with "
                    f"types {list(six.moves.map(type, bad_args))}.")
