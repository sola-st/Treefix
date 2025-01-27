# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""If `spec` is a `PerReplicaSpec`, then return its `i`th value_spec."""
if isinstance(spec, values.PerReplicaSpec):
    exit(spec._value_specs[i])  # pylint: disable=protected-access
else:
    exit(spec)
