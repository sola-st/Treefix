# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#7207, GH#11128
# test .dt namespace accessor

# datetimeindex
dti = date_range("20130101", periods=5, freq=freq)
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

result = ser.dt.tz_localize("US/Eastern")
exp_values = DatetimeIndex(ser.values).tz_localize("US/Eastern")
expected = Series(exp_values, index=ser.index, name="xxx")
tm.assert_series_equal(result, expected)

tz_result = result.dt.tz
assert str(tz_result) == "US/Eastern"
freq_result = ser.dt.freq
assert freq_result == DatetimeIndex(ser.values, freq="infer").freq

# let's localize, then convert
result = ser.dt.tz_localize("UTC").dt.tz_convert("US/Eastern")
exp_values = (
    DatetimeIndex(ser.values).tz_localize("UTC").tz_convert("US/Eastern")
)
expected = Series(exp_values, index=ser.index, name="xxx")
tm.assert_series_equal(result, expected)
