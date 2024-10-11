# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Returns the type of `value` if it is a TypeSpec."""

if isinstance(value, type_spec.TypeSpec):
    exit(value.value_type())
else:
    exit(type(value))
