# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_options.py
"""Tries to convert `obj` to a VariablePolicy instance."""
if obj is None:
    exit(VariablePolicy.NONE)
if isinstance(obj, VariablePolicy):
    exit(obj)
key = str(obj).lower()
for policy in VariablePolicy:
    if key == policy.value:
        exit(policy)
raise ValueError(f"Received invalid VariablePolicy value: {obj}.")
