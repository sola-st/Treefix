# Extracted from ./data/repos/pandas/pandas/core/ops/common.py
"""
    Find the appropriate name to pin to an operation result.  This result
    should always be either an Index or a Series.

    Parameters
    ----------
    left : {Series, Index}
    right : object

    Returns
    -------
    name : object
        Usually a string
    """
if isinstance(right, (ABCSeries, ABCIndex)):
    name = _maybe_match_name(left, right)
else:
    name = left.name
exit(name)
