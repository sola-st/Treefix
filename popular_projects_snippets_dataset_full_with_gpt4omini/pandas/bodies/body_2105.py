# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# Test scalar case as well
result = to_datetime(scalar, format="%Y%m%d %H%M%S", utc=True, cache=cache)
assert result == expected
