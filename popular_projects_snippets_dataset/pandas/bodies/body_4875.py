# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
values = Series(
    ["om", None, "foo_nom", "nom", "bar_foo", None, "foo", "regex", "rege."],
    dtype=nullable_string_dtype,
)
result = values.str.endswith("foo", na=na)
exp = Series(
    [False, na, False, False, True, na, True, False, False], dtype="boolean"
)
tm.assert_series_equal(result, exp)

result = values.str.endswith("rege.", na=na)
exp = Series(
    [False, na, False, False, False, na, False, False, True], dtype="boolean"
)
tm.assert_series_equal(result, exp)
