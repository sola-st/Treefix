# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
tz = getattr(dtype, "tz", None)

dti = pd.date_range("2016-01-01", periods=55, freq="D", tz=tz)
if tz is None:
    arr = np.asarray(dti).astype(f"M8[{unit}]")
else:
    arr = np.asarray(dti.tz_convert("UTC").tz_localize(None)).astype(
        f"M8[{unit}]"
    )

dta = DatetimeArray._simple_new(arr, dtype=dtype)
exit((dta, dti))
