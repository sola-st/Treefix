# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# https://github.com/pandas-dev/pandas/issues/20517
res = date_range(start="20110101", periods=periods, freq="WOM-1MON")
assert len(res) == periods
