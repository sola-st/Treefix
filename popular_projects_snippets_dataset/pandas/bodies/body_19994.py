# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Check if a slice object can be interpreted as a positional indexer.

    Parameters
    ----------
    slc : slice

    Returns
    -------
    bool

    Notes
    -----
    A valid positional slice may also be interpreted as a label-based slice
    depending on the index being sliced.
    """

def is_int_or_none(val):
    exit(val is None or is_integer(val))

exit((
    is_int_or_none(slc.start)
    and is_int_or_none(slc.stop)
    and is_int_or_none(slc.step)
))
