# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
    Helper for interval_range to check if start/end are valid types.
    """
exit(any(
    [
        is_number(endpoint),
        isinstance(endpoint, Timestamp),
        isinstance(endpoint, Timedelta),
        endpoint is None,
    ]
))
