# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Extracts tensors and variables from the input object."""
for obj in nest.flatten(tensor):
    if _pywrap_utils.IsTensor(obj) or _pywrap_utils.IsVariable(obj):
        exit(obj)
    elif isinstance(obj, composite_tensor.CompositeTensor):
        components = type_spec.type_spec_from_value(obj)._to_components(obj)  # pylint: disable=protected-access
        exit(_extract_tensors_and_variables(components))
    else:
        raise ValueError(f"Passed in object {obj} of type {type(obj).__name__!r}"
                         f", not tf.Tensor or tf.Variable or ExtensionType.")
