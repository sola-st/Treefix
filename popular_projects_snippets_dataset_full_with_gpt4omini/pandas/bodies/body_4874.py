# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# add category dtype parametrizations for GH-36241
values = Series(
    ["om", null_value, "foo_nom", "nom", "bar_foo", null_value, "foo"],
    dtype=dtype,
)

result = values.str.endswith(pat)
exp = Series([False, np.nan, False, False, True, np.nan, True])
tm.assert_series_equal(result, exp)

result = values.str.endswith(pat, na=na)
exp = Series([False, na, False, False, True, na, True])
tm.assert_series_equal(result, exp)

# mixed
mixed = np.array(
    ["a", np.nan, "b", True, datetime.today(), "foo", None, 1, 2.0],
    dtype=object,
)
rs = Series(mixed).str.endswith("f")
xp = Series([False, np.nan, False, np.nan, np.nan, False, np.nan, np.nan, np.nan])
tm.assert_series_equal(rs, xp)
