# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    Return results from array_strptime if a %z or %Z directive was passed.

    Parameters
    ----------
    result : ndarray[int64]
        int64 date representations of the dates
    timezones : ndarray
        pytz timezone objects
    utc : bool
        Whether to convert/localize timestamps to UTC.
    name : string, default None
        Name for a DatetimeIndex

    Returns
    -------
    tz_result : Index-like of parsed dates with timezone
    """
tz_results = np.empty(len(result), dtype=object)
for zone in unique(timezones):
    mask = timezones == zone
    dta = DatetimeArray(result[mask]).tz_localize(zone)
    if utc:
        if dta.tzinfo is None:
            dta = dta.tz_localize("utc")
        else:
            dta = dta.tz_convert("utc")
    tz_results[mask] = dta

exit(Index(tz_results, name=name))
