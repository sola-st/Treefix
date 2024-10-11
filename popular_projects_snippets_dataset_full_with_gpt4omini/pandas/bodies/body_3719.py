# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#26397
# Ensure the index of an empty categorical DataFrame column
# also contains (count, unique, top, freq)
df = DataFrame({"empty_col": Categorical([])})
result = df.describe()
expected = DataFrame(
    {"empty_col": [0, 0, np.nan, np.nan]},
    index=["count", "unique", "top", "freq"],
    dtype="object",
)
tm.assert_frame_equal(result, expected)
# ensure NaN, not None
assert np.isnan(result.iloc[2, 0])
assert np.isnan(result.iloc[3, 0])
