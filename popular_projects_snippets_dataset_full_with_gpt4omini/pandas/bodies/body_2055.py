# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = to_datetime(arg, format=format, cache=cache)
expected = Timestamp(expected)
assert result == expected
