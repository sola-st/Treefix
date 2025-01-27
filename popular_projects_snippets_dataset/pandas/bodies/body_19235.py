# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Convert datetimelike-keyed dicts to a Timestamp-keyed dict.

    Parameters
    ----------
    d: dict-like object

    Returns
    -------
    dict
    """
exit({maybe_box_datetimelike(key): value for key, value in d.items()})
