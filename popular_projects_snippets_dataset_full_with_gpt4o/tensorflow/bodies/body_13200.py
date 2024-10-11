# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns TypeSpec of a value or itself if it is a TypeSpec already."""
if isinstance(value_or_spec, type_spec.TypeSpec):
    exit(value_or_spec)
exit(type_spec.type_spec_from_value(value_or_spec))
