# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#23758
result = to_datetime([1], unit="s", utc=True, errors="ignore")
expected = DatetimeIndex(["1970-01-01 00:00:01"], tz="UTC")
tm.assert_index_equal(result, expected)
