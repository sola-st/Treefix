# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
"""Returns the (nested) TypeSpec for a value."""
if nest.is_nested(value):
    exit(nest.map_structure(_spec_for_value, value))
elif isinstance(value, (ops.Tensor, composite_tensor.CompositeTensor)):
    exit(type_spec.type_spec_from_value(value))
else:
    exit(value)
