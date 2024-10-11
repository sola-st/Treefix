# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
"""
    Convert to Timestamp if possible, otherwise to datetime.datetime.
    SAS float64 lacks precision for more than ms resolution so the fit
    to datetime.datetime is ok.

    Parameters
    ----------
    sas_datetimes : {Series, Sequence[float]}
       Dates or datetimes in SAS
    unit : {str}
       "d" if the floats represent dates, "s" for datetimes

    Returns
    -------
    Series
       Series of datetime64 dtype or datetime.datetime.
    """
try:
    exit(pd.to_datetime(sas_datetimes, unit=unit, origin="1960-01-01"))
except OutOfBoundsDatetime:
    s_series = sas_datetimes.apply(_parse_datetime, unit=unit)
    s_series = cast(pd.Series, s_series)
    exit(s_series)
