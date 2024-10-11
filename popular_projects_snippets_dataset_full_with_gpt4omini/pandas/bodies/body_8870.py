# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# pre-2.0 we required exact tz match, in 2.0 we require just
#  matching tzawareness
dti = pd.date_range("2016-01-01", periods=3, tz="UTC")
dta = dti._data

fill_value = pd.Timestamp("2020-10-18 18:44", tz="US/Pacific")

result = dta.shift(1, fill_value=fill_value)
expected = dta.shift(1, fill_value=fill_value.tz_convert("UTC"))
tm.assert_equal(result, expected)
