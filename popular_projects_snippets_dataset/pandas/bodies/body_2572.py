# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
assert (
    "A",
    "B",
) not in float_frame.columns
float_frame["A", "B"] = float_frame["A"]
assert ("A", "B") in float_frame.columns

result = float_frame["A", "B"]
expected = float_frame["A"]
tm.assert_series_equal(result, expected, check_names=False)
