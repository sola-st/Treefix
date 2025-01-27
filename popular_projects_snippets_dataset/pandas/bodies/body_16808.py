# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
target, source = target_source

merged = target.join(source, on="C")
tm.assert_series_equal(merged["MergedA"], target["A"], check_names=False)
tm.assert_series_equal(merged["MergedD"], target["D"], check_names=False)

# join with duplicates (fix regression from DataFrame/Matrix merge)
df = DataFrame({"key": ["a", "a", "b", "b", "c"]})
df2 = DataFrame({"value": [0, 1, 2]}, index=["a", "b", "c"])
joined = df.join(df2, on="key")
expected = DataFrame(
    {"key": ["a", "a", "b", "b", "c"], "value": [0, 0, 1, 1, 2]}
)
tm.assert_frame_equal(joined, expected)

# Test when some are missing
df_a = DataFrame([[1], [2], [3]], index=["a", "b", "c"], columns=["one"])
df_b = DataFrame([["foo"], ["bar"]], index=[1, 2], columns=["two"])
df_c = DataFrame([[1], [2]], index=[1, 2], columns=["three"])
joined = df_a.join(df_b, on="one")
joined = joined.join(df_c, on="one")
assert np.isnan(joined["two"]["c"])
assert np.isnan(joined["three"]["c"])

# merge column not p resent
with pytest.raises(KeyError, match="^'E'$"):
    target.join(source, on="E")

# overlap
source_copy = source.copy()
source_copy["A"] = 0
msg = (
    "You are trying to merge on float64 and object columns. If "
    "you wish to proceed you should use pd.concat"
)
with pytest.raises(ValueError, match=msg):
    target.join(source_copy, on="A")
