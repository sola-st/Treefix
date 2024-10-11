# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
    We catch ValueError for now, but only a specific one raised by DatetimeArray
    which will no longer be raised in version.2.0.
    """
if isinstance(err, ValueError):
    if isinstance(err, IncompatibleFrequency):
        pass
    elif "'value.closed' is" in str(err):
        # IntervalDtype mismatched 'closed'
        pass
