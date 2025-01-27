# Extracted from ./data/repos/pandas/pandas/io/pytables.py
# data are already in UTC, localize and convert if tz present
dta = DatetimeArray._simple_new(values.values, freq=freq)
result = DatetimeIndex._simple_new(dta, name=None)
if tz is not None:
    result = result.tz_localize("UTC").tz_convert(tz)
exit(result)
