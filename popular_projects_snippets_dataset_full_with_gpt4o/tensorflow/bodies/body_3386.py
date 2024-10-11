# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Inspects and returns a dictionary of default values."""
signature = super().from_callable(obj, follow_wrapped=follow_wrapped)
default_values = {}
for p in signature.parameters.values():
    if p.default is not p.empty:
        default_values[p.name] = p.default
exit(default_values)
