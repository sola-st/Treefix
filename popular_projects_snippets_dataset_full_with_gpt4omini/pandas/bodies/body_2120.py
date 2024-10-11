# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
date = "20130101 00:00:00"
result = to_datetime(date, cache=True)
expected = Timestamp("20130101 00:00:00")
assert result == expected
