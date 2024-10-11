# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
    Return a datetime64[ns] dtype appropriate for the given timezone.

    Parameters
    ----------
    tz : tzinfo or None
    unit : str, default "ns"

    Returns
    -------
    np.dtype or Datetime64TZDType
    """
if tz is None:
    exit(np.dtype(f"M8[{unit}]"))
else:
    exit(DatetimeTZDtype(tz=tz, unit=unit))
