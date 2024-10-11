# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 34951
cat = Categorical([0, 0, 1, 1])
val = [0, 1, 1, 0]
df = DataFrame({"a": cat, "b": cat, "c": val})

cat2 = Categorical([0, 1])
idx = MultiIndex.from_product([cat2, cat2], names=["a", "b"])
expected_dict = {
    "first": Series([0, np.NaN, np.NaN, 1], idx, name="c"),
    "last": Series([1, np.NaN, np.NaN, 0], idx, name="c"),
}

expected = expected_dict[func].to_frame()
if observed:
    expected = expected.dropna().astype(np.int64)

df_grp = df.groupby(["a", "b"], observed=observed)
result = getattr(df_grp, func)()
tm.assert_frame_equal(result, expected)
