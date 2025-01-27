# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Find non-trivial slices in "line": return a list of booleans with same length.
    """
exit([isinstance(k, slice) and not is_null_slice(k) for k in line])
