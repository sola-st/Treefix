# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
# For loaded function, structured_outputs are already specs.
if isinstance(value, type_spec.TypeSpec):
    exit(value)
exit(type_spec.type_spec_from_value(value))
