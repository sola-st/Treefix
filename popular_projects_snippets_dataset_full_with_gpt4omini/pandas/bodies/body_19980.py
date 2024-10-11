# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    Returns
    -------
    bool
    """
exit((
    obj.start is not None
    or obj.stop is not None
    or (obj.step is not None and obj.step != 1)
))
