# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# but we want to make sure that we are coercing
# if we have ints/strings
expected = DatetimeIndex(exp)
with tm.assert_produces_warning(warning, match="Could not infer format"):
    result = to_datetime(arr, errors="coerce", cache=cache)
tm.assert_index_equal(result, expected)
