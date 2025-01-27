# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# https://github.com/pandas-dev/pandas/pull/48748#issuecomment-1260181008
td = pd.Timedelta(microseconds=1)
dti = pd.date_range("2016-01-01", periods=3) - td
dta = dti._data.as_unit("us")

res = dta + td.as_unit("us")
# even though the result is an even number of days
#  (so we _could_ downcast to unit="s"), we do not.
assert res.unit == "us"
