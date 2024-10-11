# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# GH8989
# truncating the nanoseconds when a format was provided
expected = to_datetime(arg, cache=cache)
result = to_datetime(arg, format="%Y-%m-%d %H:%M:%S.%f", cache=cache)
assert result == expected
