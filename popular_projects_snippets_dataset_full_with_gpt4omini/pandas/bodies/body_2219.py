# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
with tm.assert_produces_warning(warning, match="Could not infer format"):
    result = to_datetime(expected, errors="ignore", format=format, cache=cache)
assert result == expected
