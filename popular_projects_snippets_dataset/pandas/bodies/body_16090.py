# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#11295
# ambiguous time error on the conversions
ser = Series(date_range("2015-01-01", "2016-01-01", freq="T"), name="xxx")
ser = ser.dt.tz_localize("UTC").dt.tz_convert("America/Chicago")

exp_values = date_range(
    "2015-01-01", "2016-01-01", freq="T", tz="UTC"
).tz_convert("America/Chicago")
# freq not preserved by tz_localize above
exp_values = exp_values._with_freq(None)
expected = Series(exp_values, name="xxx")
tm.assert_series_equal(ser, expected)
