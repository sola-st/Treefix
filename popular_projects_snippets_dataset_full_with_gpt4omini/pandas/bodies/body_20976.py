# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
    Localize a start or end Timestamp to the timezone of the corresponding
    start or end Timestamp

    Parameters
    ----------
    ts : start or end Timestamp to potentially localize
    is_none : argument that should be None
    is_not_none : argument that should not be None
    freq : Tick, DateOffset, or None
    tz : str, timezone object or None
    ambiguous: str, localization behavior for ambiguous times
    nonexistent: str, localization behavior for nonexistent times

    Returns
    -------
    ts : Timestamp
    """
# Make sure start and end are timezone localized if:
# 1) freq = a Timedelta-like frequency (Tick)
# 2) freq = None i.e. generating a linspaced range
if is_none is None and is_not_none is not None:
    # Note: We can't ambiguous='infer' a singular ambiguous time; however,
    # we have historically defaulted ambiguous=False
    ambiguous = ambiguous if ambiguous != "infer" else False
    localize_args = {"ambiguous": ambiguous, "nonexistent": nonexistent, "tz": None}
    if isinstance(freq, Tick) or freq is None:
        localize_args["tz"] = tz
    ts = ts.tz_localize(**localize_args)
exit(ts)
