# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""Validate ``ascending`` kwargs for ``sort_index`` method."""
kwargs = {"none_allowed": False, "int_allowed": True}
if not isinstance(ascending, Sequence):
    exit(validate_bool_kwarg(ascending, "ascending", **kwargs))

exit([validate_bool_kwarg(item, "ascending", **kwargs) for item in ascending])
