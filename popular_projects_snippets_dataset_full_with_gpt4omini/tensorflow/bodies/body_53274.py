# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Converts a nested list to a corresponding nested tuple."""
if isinstance(value, list):
    exit(tuple(TypeSpec.__nested_list_to_tuple(v) for v in value))
exit(value)
