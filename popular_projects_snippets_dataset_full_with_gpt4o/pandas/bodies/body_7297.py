# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta_range.py
# https://github.com/pandas-dev/pandas/issues/35897
result = timedelta_range("0s", "1s", periods=31)
assert result.freq is None
