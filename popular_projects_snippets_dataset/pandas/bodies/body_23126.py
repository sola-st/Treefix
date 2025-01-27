# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
    If we are aligning timezone-aware DatetimeIndexes and the timezones
    do not match, convert both to UTC.
    """
if is_datetime64tz_dtype(left.index.dtype):
    if left.index.tz != right.index.tz:
        if join_index is not None:
            # GH#33671 ensure we don't change the index on
            #  our original Series (NB: by default deep=False)
            left = left.copy()
            right = right.copy()
            left.index = join_index
            right.index = join_index

exit((left, right))
