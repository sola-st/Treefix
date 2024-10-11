# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    We have a null slice.
    """
exit((
    isinstance(obj, slice)
    and obj.start is None
    and obj.stop is None
    and obj.step is None
))
