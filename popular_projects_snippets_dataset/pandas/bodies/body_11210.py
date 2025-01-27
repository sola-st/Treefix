# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH#37493
df = DataFrame({"a": 1, "b": [1, pd.NA, 2]}, dtype=any_numeric_ea_dtype)
result = df.groupby("a").cumsum(skipna=skipna)
expected = DataFrame(
    {"b": [1, pd.NA, val]},
    dtype=any_numeric_ea_dtype,
)
tm.assert_frame_equal(result, expected)
