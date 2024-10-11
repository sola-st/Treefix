# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#7207, GH#11128
# test .dt namespace accessor

# datetimeindex with tz
dti = date_range("20130101", periods=5, tz="US/Eastern")
ser = Series(dti, name="xxx")
for prop in ok_for_dt:

    # we test freq below
    if prop != "freq":
        self._compare(ser, prop)

for prop in ok_for_dt_methods:
    getattr(ser.dt, prop)

result = ser.dt.to_pydatetime()
assert isinstance(result, np.ndarray)
assert result.dtype == object

result = ser.dt.tz_convert("CET")
expected = Series(ser._values.tz_convert("CET"), index=ser.index, name="xxx")
tm.assert_series_equal(result, expected)

tz_result = result.dt.tz
assert str(tz_result) == "CET"
freq_result = ser.dt.freq
assert freq_result == DatetimeIndex(ser.values, freq="infer").freq
