# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# gh-18450
s = Series(["foo,bar,baz", np.nan], dtype=any_string_dtype)
result = s.str.split(",", expand=True)
exp = DataFrame(
    [["foo", "bar", "baz"], [np.nan, np.nan, np.nan]], dtype=any_string_dtype
)
tm.assert_frame_equal(result, exp)

# check that these are actually np.nan/pd.NA and not None
# TODO see GH 18463
# tm.assert_frame_equal does not differentiate
if any_string_dtype == "object":
    assert all(np.isnan(x) for x in result.iloc[1])
else:
    assert all(x is pd.NA for x in result.iloc[1])
