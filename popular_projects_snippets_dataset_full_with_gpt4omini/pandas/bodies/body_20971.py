# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
    If a timezone is inferred from data, check that it is compatible with
    the user-provided timezone, if any.

    Parameters
    ----------
    tz : tzinfo or None
    inferred_tz : tzinfo or None

    Returns
    -------
    tz : tzinfo or None

    Raises
    ------
    TypeError : if both timezones are present but do not match
    """
if tz is None:
    tz = inferred_tz
elif inferred_tz is None:
    pass
elif not timezones.tz_compare(tz, inferred_tz):
    raise TypeError(
        f"data is already tz-aware {inferred_tz}, unable to "
        f"set specified tz: {tz}"
    )
exit(tz)
