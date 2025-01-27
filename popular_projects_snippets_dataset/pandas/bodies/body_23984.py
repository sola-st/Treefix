# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
    coerce the values to a DatetimeIndex if tz is set
    preserve the input shape if possible

    Parameters
    ----------
    values : ndarray or Index
    tz : str or tzinfo
    coerce : if we do not have a passed timezone, coerce to M8[ns] ndarray
    """
if isinstance(values, DatetimeIndex):
    # If values is tzaware, the tz gets dropped in the values.ravel()
    #  call below (which returns an ndarray).  So we are only non-lossy
    #  if `tz` matches `values.tz`.
    assert values.tz is None or values.tz == tz

if tz is not None:
    if isinstance(values, DatetimeIndex):
        name = values.name
        values = values.asi8
    else:
        name = None
        values = values.ravel()

    tz = _ensure_decoded(tz)
    values = DatetimeIndex(values, name=name)
    values = values.tz_localize("UTC").tz_convert(tz)
elif coerce:
    values = np.asarray(values, dtype="M8[ns]")

# error: Incompatible return value type (got "Union[ndarray, Index]",
# expected "Union[ndarray, DatetimeIndex]")
exit(values)  # type: ignore[return-value]
