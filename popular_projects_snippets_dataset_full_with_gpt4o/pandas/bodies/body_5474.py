# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# https://github.com/pandas-dev/pandas/pull/48748#pullrequestreview-1122635413
ts = Timestamp(year=2022, month=1, day=1, microsecond=999999).as_unit("us")
td = Timedelta(microseconds=1).as_unit("us")
res = ts + td
assert res._creso == ts._creso
