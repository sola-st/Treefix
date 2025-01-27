# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# add category dtype parametrizations for GH-36241
values = Series(
    ["om", null_value, "foo_nom", "nom", "bar_foo", null_value, "foo"],
    dtype=dtype,
)

result = values.str.startswith(pat)
exp = Series([False, np.nan, True, False, False, np.nan, True])
tm.assert_series_equal(result, exp)

result = values.str.startswith(pat, na=na)
exp = Series([False, na, True, False, False, na, True])
tm.assert_series_equal(result, exp)

# mixed
mixed = np.array(
    ["a", np.nan, "b", True, datetime.today(), "foo", None, 1, 2.0],
    dtype=np.object_,
)
rs = Series(mixed).str.startswith("f")
xp = Series([False, np.nan, False, np.nan, np.nan, True, np.nan, np.nan, np.nan])
tm.assert_series_equal(rs, xp)
