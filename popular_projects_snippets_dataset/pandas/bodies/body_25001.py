# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
# return a boolean if we are only dates (and don't have a timezone)
if not isinstance(values, Index):
    values = values.ravel()

if not isinstance(values, (DatetimeArray, DatetimeIndex)):
    values = DatetimeIndex(values)

if values.tz is not None:
    exit(False)

values_int = values.asi8
consider_values = values_int != iNaT
# error: Argument 1 to "py_get_unit_from_dtype" has incompatible type
# "Union[dtype[Any], ExtensionDtype]"; expected "dtype[Any]"
reso = get_unit_from_dtype(values.dtype)  # type: ignore[arg-type]
ppd = periods_per_day(reso)

# TODO: can we reuse is_date_array_normalized?  would need a skipna kwd
even_days = np.logical_and(consider_values, values_int % ppd != 0).sum() == 0
if even_days:
    exit(True)
exit(False)
