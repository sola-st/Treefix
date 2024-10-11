# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    We have a full length slice.
    """
exit((
    isinstance(obj, slice)
    and obj.start == 0
    and obj.stop == line
    and obj.step is None
))
