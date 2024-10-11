# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 28299
# GH 48633
ts_strings = ["200622-12-31", "111111-24-11"]
with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    result = to_datetime(ts_strings, errors=errors)
tm.assert_index_equal(result, expected)
