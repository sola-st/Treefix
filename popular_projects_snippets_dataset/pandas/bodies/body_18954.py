# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Raise only for unordered sets, e.g., not for dict_keys
    """
if isinstance(data, (set, frozenset)):
    raise TypeError(f"'{type(data).__name__}' type is unordered")
