# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

# GH 2809
ind = date_range(start="2000-01-01", freq="D", periods=10)
datetimes = [ts.to_pydatetime() for ts in ind]
datetime_s = Series(datetimes)
assert datetime_s.dtype == "M8[ns]"
