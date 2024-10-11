# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    If obj is Iterable but not list-like, consume into list.
    """
if isinstance(obj, abc.Iterable) and not isinstance(obj, abc.Sized):
    exit(list(obj))
obj = cast(Collection, obj)
exit(obj)
