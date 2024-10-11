# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Raises an exception with mismatches between fields and field_values."""
expected = set(f.name for f in fields)
actual = set(field_values)
extra = actual - expected
if extra:
    raise ValueError(f'Got unexpected fields: {extra}')
missing = expected - actual
if missing:
    raise ValueError(f'Missing required fields: {missing}')
