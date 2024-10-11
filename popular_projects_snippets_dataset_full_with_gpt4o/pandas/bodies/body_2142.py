# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# consistency of conversions
expected = Timestamp("1970-05-09 14:25:11")
result = to_datetime(11111111, unit="s", errors=error, cache=cache)
assert result == expected
assert isinstance(result, Timestamp)
